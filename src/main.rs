extern crate phyloalifold;
extern crate bio;
extern crate num_cpus;

use phyloalifold::*;
use std::env;
use std::path::Path;
use std::io::prelude::*;
use std::io::{BufReader, BufWriter};
use std::fs::File;
use bio::io::fasta::Reader;

type MeaCssStr = MeaSsStr;
type Strings = Vec<String>;

const DEFAULT_GAMMA: Prob = 1.;
const DEFAULT_PROB_WEIGHT: Prob = 0.5;

fn main() {
  let args = env::args().collect::<Vec<Arg>>();
  let program_name = args[0].clone();
  let mut opts = Options::new();
  opts.reqopt("i", "input_file_path", "The path to an input FASTA file that contains RNA sequences", "STR");
  opts.reqopt("a", "input_seq_align_file_path", "The path to an input CLUSTAL file containing a sequence alignment of RNA sequences", "STR");
  opts.reqopt("c", "input_pair_prob_matrix_file_path", "The path to an input file containing pairing probability matrices computed by the RNAalipfold algorithm", "STR");
  opts.reqopt("o", "output_file_path", "The path to an output STOCKHOLM file which will contain estimated consensus secondary structures", "STR");
  opts.optopt("", "opening_gap_penalty", &format!("An opening-gap penalty (Uses {} by default)", DEFAULT_OPENING_GAP_PENALTY), "FLOAT");
  opts.optopt("", "extending_gap_penalty", &format!("An extending-gap penalty (Uses {} by default)", DEFAULT_EXTENDING_GAP_PENALTY), "FLOAT");
  opts.optopt("", "min_base_pair_prob", &format!("A minimum base-pairing-probability (Uses {} by default)", DEFAULT_MIN_BPP), "FLOAT");
  opts.optopt("", "offset_4_max_gap_num", &format!("An offset for maximum numbers of gaps (Uses {} by default)", DEFAULT_OFFSET_4_MAX_GAP_NUM), "UINT");
  opts.optopt("", "gamma", &format!("An MEA gamma (Uses {} by default)", DEFAULT_GAMMA), "FLOAT");
  opts.optopt("", "prob_weight", &format!("A probability weight (Uses {} by default)", DEFAULT_PROB_WEIGHT), "FLOAT");
  opts.optopt("t", "num_of_threads", "The number of threads in multithreading (Uses the number of all the threads of this computer by default)", "UINT");
  opts.optflag("h", "help", "Print a help menu");
  let matches = match opts.parse(&args[1 ..]) {
    Ok(opt) => {opt}
    Err(failure) => {print_program_usage(&program_name, &opts); panic!(failure.to_string())}
  };
  if matches.opt_present("h") {
    print_program_usage(&program_name, &opts);
    return;
  }
  let input_file_path = matches.opt_str("i").unwrap();
  let input_file_path = Path::new(&input_file_path);
  let input_sa_file_path = matches.opt_str("a").unwrap();
  let input_sa_file_path = Path::new(&input_sa_file_path);
  let input_bpp_mat_file_path = matches.opt_str("c").unwrap();
  let input_bpp_mat_file_path = Path::new(&input_bpp_mat_file_path);
  let output_file_path = matches.opt_str("o").unwrap();
  let output_file_path = Path::new(&output_file_path);
  let opening_gap_penalty = if matches.opt_present("opening_gap_penalty") {
    matches.opt_str("opening_gap_penalty").unwrap().parse().unwrap()
  } else {
    DEFAULT_OPENING_GAP_PENALTY
  };
  let extending_gap_penalty = if matches.opt_present("extending_gap_penalty") {
    matches.opt_str("extending_gap_penalty").unwrap().parse().unwrap()
  } else {
    DEFAULT_EXTENDING_GAP_PENALTY
  };
  let min_bpp = if matches.opt_present("min_base_pair_prob") {
    matches.opt_str("min_base_pair_prob").unwrap().parse().unwrap()
  } else {
    DEFAULT_MIN_BPP
  };
  let offset_4_max_gap_num = if matches.opt_present("offset_4_max_gap_num") {
    matches.opt_str("offset_4_max_gap_num").unwrap().parse().unwrap()
  } else {
    DEFAULT_OFFSET_4_MAX_GAP_NUM
  };
  let gamma = if matches.opt_present("gamma") {
    matches.opt_str("gamma").unwrap().parse().unwrap()
  } else {
    DEFAULT_GAMMA
  };
  let prob_weight = if matches.opt_present("prob_weight") {
    matches.opt_str("prob_weight").unwrap().parse().unwrap()
  } else {
    DEFAULT_PROB_WEIGHT
  };
  let num_of_threads = if matches.opt_present("t") {
    matches.opt_str("t").unwrap().parse().unwrap()
  } else {
    num_cpus::get() as NumOfThreads
  };
  let fasta_file_reader = Reader::from_file(Path::new(&input_file_path)).unwrap();
  let mut fasta_records = FastaRecords::new();
  for fasta_record in fasta_file_reader.records() {
    let fasta_record = fasta_record.unwrap();
    let mut seq = convert(fasta_record.seq());
    seq.insert(0, PSEUDO_BASE);
    seq.push(PSEUDO_BASE);
    fasta_records.push(FastaRecord::new(String::from(fasta_record.id()), seq));
  }
  let mut thread_pool = Pool::new(num_of_threads);
  let (bpp_mats, upp_mats) = phyloprob(&mut thread_pool, &fasta_records, opening_gap_penalty, extending_gap_penalty, min_bpp, offset_4_max_gap_num);
  let (mut sa, seq_ids) = read_sa_from_clustal_file(input_sa_file_path);
  let num_of_rnas = sa.cols[0].len();
  let mut seq_lens = vec![0 as usize; num_of_rnas];
  let num_of_cols = sa.cols.len();
  sa.pos_map_sets = vec![vec![0; num_of_rnas]; num_of_cols];
  for i in 0 .. num_of_cols {
    for j in 0 .. num_of_rnas {
      let base = sa.cols[i][j];
      if base != GAP {
        seq_lens[j] += 1;
      }
      if seq_lens[j] > 0 {
        sa.pos_map_sets[i][j] = seq_lens[j] as Pos - 1;
      }
    }
  }
  let mean_bpp_mat = get_mean_bpp_mat(&bpp_mats, &sa);
  let mean_upp_mat = get_mean_upp_mat(&upp_mats, &sa);
  let sa_len = sa.cols.len();
  let num_of_rnas = sa.cols[0].len();
  let mut rnaalipfold_bpp_mat = vec![vec![0.; sa_len]; sa_len];
  let reader_2_input_bpp_mat_file = BufReader::new(File::open(input_bpp_mat_file_path).unwrap());
  for (i, vec) in reader_2_input_bpp_mat_file.split(b'\n').enumerate() {
    let vec = vec.unwrap();
    let substrings = unsafe {String::from_utf8_unchecked(vec).split_whitespace().map(|string| {String::from(string)}).collect::<Strings>()};
    for subsubstring in &substrings[2 ..] {
      let subsubsubstrings = subsubstring.split(":").collect::<Vec<&str>>();
      let j = subsubsubstrings[0].parse::<usize>().unwrap() - 1;
      rnaalipfold_bpp_mat[i][j] = subsubsubstrings[1].parse().unwrap();
    }
  }
  let mea_css = phyloalifold(&mean_bpp_mat, &mean_upp_mat, &rnaalipfold_bpp_mat, gamma, prob_weight, &sa);
  let mut writer_2_output_file = BufWriter::new(File::create(output_file_path).unwrap());
  let mut buf_4_writer_2_output_file = format!("# STOCKHOLM 1.0\n");
  let sa_len = sa.cols.len();
  let max_seq_id_len = seq_ids.iter().map(|seq_id| {seq_id.len()}).max().unwrap();
  for rna_id in 0 .. num_of_rnas {
    let ref seq_id = seq_ids[rna_id];
    buf_4_writer_2_output_file.push_str(seq_id);
    let mut stockholm_row = vec![' ' as Char; max_seq_id_len - seq_id.len() + 2];
    let mut sa_row = (0 .. sa_len).map(|x| {sa.cols[x][rna_id]}).collect::<Vec<u8>>();
    stockholm_row.append(&mut sa_row);
    let stockholm_row = unsafe {from_utf8_unchecked(&stockholm_row)};
    buf_4_writer_2_output_file.push_str(&stockholm_row);
    buf_4_writer_2_output_file.push_str("\n");
  }
  let descriptor = "#=GC SS_cons";
  let descriptor_len = descriptor.len();
  buf_4_writer_2_output_file.push_str(descriptor);
  let mut stockholm_row = vec![' ' as Char; max_seq_id_len - descriptor_len + 2];
  let mut mea_css_str = get_mea_css_str(&mea_css, sa_len);
  stockholm_row.append(&mut mea_css_str);
  let stockholm_row = unsafe {from_utf8_unchecked(&stockholm_row)};
  buf_4_writer_2_output_file.push_str(&stockholm_row);
  buf_4_writer_2_output_file.push_str("\n//");
  let _ = writer_2_output_file.write_all(buf_4_writer_2_output_file.as_bytes());
}

#[inline]
fn read_sa_from_clustal_file(clustal_file_path: &Path) -> (SeqAlign, SeqIds) {
  let mut sa = SeqAlign::new();
  let mut seq_ids = SeqIds::new();
  let reader_2_clustal_file = BufReader::new(File::open(clustal_file_path).unwrap());
  let mut seq_pointer = 0;
  let mut pos_pointer = 0;
  let mut are_seq_ids_read = false;
  for (i, string) in reader_2_clustal_file.lines().enumerate() {
    let string = string.unwrap();
    if i == 0 || string.len() == 0 || string.starts_with(" ") {
      if sa.cols.len() > 0 {
        seq_pointer = 0;
        pos_pointer = sa.cols.len();
        are_seq_ids_read = true;
      }
      continue;
    }
    let mut substrings = string.split_whitespace();
    let substring = substrings.next().unwrap();
    if !are_seq_ids_read {
      seq_ids.push(String::from(substring));
    }
    let substring = substrings.next().unwrap();
    if seq_pointer == 0 {
      for sa_char in substring.chars() {
        sa.cols.push(vec![sa_char as Char]);
      }
      seq_pointer += 1;
    } else {
      for (j, sa_char) in substring.chars().enumerate() {
        sa.cols[pos_pointer + j].push(sa_char as Char);
      }
    }
  }
  (sa, seq_ids)
}

#[inline]
fn get_mean_bpp_mat(bpp_mats: &ProbMatsWithRnaIds, sa: &SeqAlign) -> ProbMat {
  let sa_len = sa.cols.len();
  let num_of_rnas = sa.cols[0].len();
  let mut mean_bpp_mat = vec![vec![0.; sa_len]; sa_len];
  for i in 0 .. sa_len {
    for j in i + 1 .. sa_len {
      let mut mean_bpp = 0.;
      let mut effective_num_of_rnas = 0;
      for k in 0 .. num_of_rnas {
        if sa.cols[i][k] == GAP || sa.cols[j][k] == GAP {continue;}
        let ref bpp_mat = bpp_mats[k];
        let pos_pair = (sa.pos_map_sets[i][k] + 1, sa.pos_map_sets[j][k] + 1);
        match bpp_mat.get(&pos_pair) {
          Some(&bpp) => {
            mean_bpp += bpp;
            effective_num_of_rnas += 1;
          }, None => {},
        }
      }
      if effective_num_of_rnas > 0 {
        mean_bpp_mat[i][j] = mean_bpp / effective_num_of_rnas as Prob;
      }
    }
  }
  mean_bpp_mat
}

#[inline]
fn get_mean_upp_mat(upp_mats: &ProbsWithRnaIds, sa: &SeqAlign) -> Probs {
  let sa_len = sa.cols.len();
  let num_of_rnas = sa.cols[0].len();
  let mut mean_upp_mat = vec![0.; sa_len];
  for i in 0 .. sa_len {
    let mut mean_upp = 0.;
    let mut effective_num_of_rnas = 0;
    for j in 0 .. num_of_rnas {
      if sa.cols[i][j] == GAP {continue;}
      mean_upp += upp_mats[j][sa.pos_map_sets[i][j] as usize + 1];
      effective_num_of_rnas += 1;
    }
    if effective_num_of_rnas > 0 {
      mean_upp_mat[i] = mean_upp / num_of_rnas as Prob;
    }
  }
  mean_upp_mat
}

#[inline]
fn get_mea_css_str(mea_css: &MeaCss, sa_len: usize) -> MeaCssStr {
  let mut mea_css_str = vec![UNPAIRING_BASE; sa_len];
  for &(i, j) in &mea_css.bpa_pos_pairs {
    mea_css_str[i as usize] = BASE_PAIRING_LEFT_BASE;
    mea_css_str[j as usize] = BASE_PAIRING_RIGHT_BASE;
  }
  mea_css_str
}

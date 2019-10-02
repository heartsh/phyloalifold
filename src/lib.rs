extern crate rnafamprob;
extern crate neofold;
/* extern crate petgraph;
extern crate itertools; */

pub use rnafamprob::*;
pub use neofold::*;
/* pub use petgraph::graph::{Graph, NodeIndex};
pub use petgraph::Directed;
use itertools::Itertools; */

// pub type Mea = Prob;
/* pub type Col = Pos;
pub type ColQuadruple = (Col, Col, Col, Col);
pub type ColQuadruples = Vec<ColQuadruple>; 
pub type ColQuadrupleSeqsWithColQuadruples = HashMap<ColQuadruple, ColQuadruples, Hasher>; 
pub type ColPair = (Col, Col);
pub type ColPairs = Vec<ColPair>;
pub type ColPairSeqsWithColPairs = HashMap<ColPair, ColPairs, Hasher>;
pub type RnaIdPosTriple = (RnaId, Pos, Pos);
pub type RnaIdPosTriples = Vec<RnaIdPosTriple>;
pub type RnaIdPosTripleSeqsWithColPairs = HashMap<ColPair, RnaIdPosTriples, Hasher>;
pub type RnaIds = Vec<RnaId>;
#[derive(Clone)]
pub struct MeaCss {
  // pub corresponding_col_quadruple_seqs_inside_col_quadruples: ColQuadrupleSeqsWithColQuadruples,
  pub seq_num: usize,
  pub mea: Mea,
  // pub rna_id_pos_pair_seqs_with_cols: RnaIdPosPairSeqs,
  // pub rna_id_pos_triple_seqs_with_col_pairs: RnaIdPosTripleSeqsWithColPairs,
  // pub pos_pair_seqs_with_col_pairs: FloatPosPairSeqsWithColPairs,
  pub pos_pair_seqs: FloatPosPairSeqs,
  pub pos_seqs_with_cols: FloatPosSeqs,
  pub col_num: usize,
  pub rna_ids: RnaIds,
  // pub pseudo_col_quadruple: ColQuadruple,
} */
pub type Prob4dMatsWithRnaIdPairs = HashMap<RnaIdPair, Prob4dMat, Hasher>;
pub type ProbsWithRnaIds = Vec<Probs>;
/* pub type MeaCssPair<'a> = (&'a MeaCss, &'a MeaCss);
pub type Meas = Vec<Mea>;
pub type MeaMat = Vec<Meas>;
pub type Mea4dMat = HashMap<ColQuadruple, Mea, Hasher>;
pub type ClusterIndex = RnaId;
pub type ClusterIndexes = Vec<ClusterIndex>;
pub type ClusterScore = Mea;
pub type GuideTree = Graph<ClusterScore, ClusterScore, Directed, usize>;
type ClusterIndexPair = (ClusterIndex, ClusterIndex);
type ClusterScoreMat = HashMap<ClusterIndexPair, ClusterScore, Hasher>;
struct ClusterIndexScorePair {
  pub index: ClusterIndex,
  pub score: ClusterScore,
}
type ClusterIndexScorePairs = Vec<ClusterIndexScorePair>;
type ClusterIndexScorePairSeqsWithClusterIndexes = HashMap<ClusterIndex, ClusterIndexScorePairs, Hasher>;
pub type SparseMeaMat = HashMap<RnaIdPair, Mea>;
type SeqNumsWithClusterIndexes = HashMap<ClusterIndex, usize, Hasher>;
type RnaIdPosPair = (RnaId, Pos);
type RnaIdPosPairs = Vec<RnaIdPosPair>;
type RnaIdPosPairSeqs = Vec<RnaIdPosPairs>;
pub type BoolsWithPosPairs = HashMap<PosPair, bool, Hasher>;
pub type ProbSeqsWithRnaIds = Vec<Probs>;
pub type FloatPos = f32;
pub type FloatPosPair = (FloatPos, FloatPos);
pub type FloatPosPairs = Vec<FloatPosPair>;
pub type FloatPosPairSeqsWithColPairs = HashMap<ColPair, FloatPosPairs, Hasher>;
pub type FloatPoss = Vec<FloatPos>;
pub type FloatPosSeqs = Vec<FloatPoss>;
// pub type FloatPosSeqsWithCols = HashMap<Col, FloatPoss, Hasher>;
pub type FloatPosPairSeqs = Vec<FloatPosPairs>;
pub type ProbsWithCols = HashMap<Col, Prob, Hasher>; */
pub type SeqId = String;
pub type SeqIds = Vec<SeqId>;
// type FastaRecord = (FastaId, Seq, usize);
// type FastaRecords = Vec<FastaRecord>;
pub type Col = Vec<Char>;
pub type Cols = Vec<Col>;
pub type PosMaps = Vec<Pos>;
pub type PosMapSets = Vec<PosMaps>;
#[derive(Debug)]
pub struct SeqAlign {
  // pub seq_ids: SeqIds,
  pub cols: Cols,
  pub pos_map_sets: PosMapSets,
}
pub struct MeaCss {
  pub bpa_pos_pair_seqs_inside_pos_pairs: PosPairSeqsWithPosPairs,
  pub ea: Mea,
}

impl SeqAlign {
  pub fn new() -> SeqAlign {
    SeqAlign {
      // seq_ids: SeqIds::new(),
      cols: Cols::new(),
      pos_map_sets: PosMapSets::new(),
    }
  }
}

impl MeaCss {
  pub fn new() -> MeaCss {
    MeaCss {
      bpa_pos_pair_seqs_inside_pos_pairs: PosPairSeqsWithPosPairs::default(),
      ea: 0.,
    }
  }
}

/* impl MeaCss {
  pub fn new() -> MeaCss {
    MeaCss {
      // corresponding_col_quadruple_seqs_inside_col_quadruples: ColQuadrupleSeqsWithColQuadruples::default(),
      seq_num: 0,
      mea: 0.,
      /* rna_id_pos_pair_seqs_with_cols: RnaIdPosPairSeqs::new(),
      rna_id_pos_triple_seqs_with_col_pairs: RnaIdPosTripleSeqsWithColPairs::default(), */
      pos_pair_seqs: FloatPosPairSeqs::new(),
      pos_seqs_with_cols: FloatPosSeqs::new(),
      col_num: 0,
      rna_ids: RnaIds::new(),
      // pseudo_col_quadruple: (0, 0, 0, 0),
    }
  }
} */

/* impl ClusterIndexScorePair {
  pub fn new(cluster_index: ClusterIndex, cluster_score: ClusterScore) -> ClusterIndexScorePair {
    ClusterIndexScorePair {
      index: cluster_index,
      score: cluster_score,
    }
  }
} */

pub const GAP: Char = '-' as Char;

#[inline]
pub fn neoalifold(bpap_mats_with_rna_id_pairs: &Prob4dMatsWithRnaIdPairs, mean_upp_mat: &Probs, gamma: Prob, sa: &SeqAlign) -> MeaCss {
  let mut mea_mat_4_bpa_pos_pairs = MeaMat::default();
  let mut pos_seqs_with_poss_4_forward_bpas = PosSeqsWithPoss::default();
  let sa_len = sa.cols.len();
  let num_of_rnas = sa.cols[0].len();
  let combination_num = (num_of_rnas * (num_of_rnas - 1)) as Prob / 2.;
  for sub_sa_len in 2 .. sa_len + 1 {
    for i in 0 .. sa_len + 1 - sub_sa_len {
      let j = i + sub_sa_len - 1;
      let pos_pair = (i, j);
      let mut mean_bpap = 0.;
      for rna_id_1 in 0 .. num_of_rnas {
        for rna_id_2 in rna_id_1 + 1 .. num_of_rnas {
          let rna_id_pair = (rna_id_1, rna_id_2);
          let ref bpap_mat = bpap_mats_with_rna_id_pairs[&rna_id_pair];
          let base_quadruple = (sa.cols[i][rna_id_1], sa.cols[j][rna_id_1], sa.cols[i][rna_id_2], sa.cols[j][rna_id_2]);
          if base_quadruple.0 == GAP || base_quadruple.1 == GAP || base_quadruple.2 == GAP || base_quadruple.3 == GAP {
            continue;
          }
          let pos_quadruple = (sa.pos_map_sets[i][rna_id_1], sa.pos_map_sets[j][rna_id_1], sa.pos_map_sets[i][rna_id_2], sa.pos_map_sets[j][rna_id_2]);
          match bpap_mat.get(&pos_quadruple) {
            Some(&bpap) => {
              mean_bpap += bpap;
            },
            None => {},
          }
        }
      }
      mean_bpap /= combination_num;
      let meas_4_bpa_pos_pair = get_meas_4_bpa_pos_pair(&pos_pair, &mea_mat_4_bpa_pos_pairs, &pos_seqs_with_poss_4_forward_bpas, mean_upp_mat);
      mea_mat_4_bpa_pos_pairs.insert(pos_pair, meas_4_bpa_pos_pair[j - i - 1] + gamma * mean_bpap);
      let poss_exist = match pos_seqs_with_poss_4_forward_bpas.get(&j) {
        Some(_) => {true},
        None => {false},
      };
      if poss_exist {
        pos_seqs_with_poss_4_forward_bpas.get_mut(&j).expect("Failed to get an element of a hash map.").push(i);
      } else {
        pos_seqs_with_poss_4_forward_bpas.insert(j, vec![i]);
      }
      /* match bpp_mat.get(&pos_pair) {
        Some(&bpp) => {
          let meas_4_bp_pos_pair = get_meas_4_bp_pos_pair(&pos_pair, &mea_mat_4_bp_pos_pairs, &pos_seqs_with_poss_4_forward_bps, upp_mat);
          mea_mat_4_bp_pos_pairs.insert(pos_pair, meas_4_bp_pos_pair[j - i - 1] + gamma * bpp);
          let poss_exist = match pos_seqs_with_poss_4_forward_bps.get(&j) {
            Some(_) => {true},
            None => {false},
          };
          if poss_exist {
            pos_seqs_with_poss_4_forward_bps.get_mut(&j).expect("Failed to get an element of a hash map.").push(i);
          } else {
            pos_seqs_with_poss_4_forward_bps.insert(j, vec![i]);
          }
        },
        None => {},
      } */
    }
  }
  let mut mea_css = MeaCss::new();
  let pseudo_pos_pair = (0, sa_len - 1);
  let mut pos_pair_stack = vec![pseudo_pos_pair];
  while pos_pair_stack.len() > 0 {
    let pos_pair_1 = pos_pair_stack.pop().expect("Failed to pop an element of a vector.");
    let meas_4_bpa_pos_pair = get_meas_4_bpa_pos_pair(&pos_pair_1, &mea_mat_4_bpa_pos_pairs, &pos_seqs_with_poss_4_forward_bpas, mean_upp_mat);
    let (i, j) = pos_pair_1;
    let mea = meas_4_bpa_pos_pair[j - i - 1];
    if mea == 0. {continue;}
    let mut n = j - 1;
    while meas_4_bpa_pos_pair[n - i] > 0. {
      let mea = meas_4_bpa_pos_pair[n - i];
      if mea == meas_4_bpa_pos_pair[n - i - 1] + mean_upp_mat[n] {
        n = n - 1;
      } else {
        match pos_seqs_with_poss_4_forward_bpas.get(&n) {
          Some(poss) => {
            for &m in poss {
              if m <= i {continue;}
              let pos_pair_2 = (m, n);
              if mea == meas_4_bpa_pos_pair[m - i - 1] + mea_mat_4_bpa_pos_pairs[&pos_pair_2] {
                let bpa_pos_pairs_exist = match mea_css.bpa_pos_pair_seqs_inside_pos_pairs.get(&pos_pair_1) {
                  Some(_) => {true},
                  None => {false},
                };
                if bpa_pos_pairs_exist {
                  mea_css.bpa_pos_pair_seqs_inside_pos_pairs.get_mut(&pos_pair_1).expect("Failed to get an element of a hash map.").push(pos_pair_2);
                } else {
                  mea_css.bpa_pos_pair_seqs_inside_pos_pairs.insert(pos_pair_1, vec![pos_pair_2]);
                }
                pos_pair_stack.push(pos_pair_2);
                n = m - 1;
                break;
              }
            }
          },
          None => {},
        }
      }
    }
  }
  mea_css.ea = mea_mat_4_bpa_pos_pairs[&pseudo_pos_pair];
  mea_css
}

fn get_meas_4_bpa_pos_pair(pos_pair: &PosPair, mea_mat_4_bpa_pos_pairs: &MeaMat, pos_seqs_with_poss_4_forward_bpas: &PosSeqsWithPoss, mean_upp_mat: &Probs) -> Meas {
  let (i, j) = *pos_pair;
  let sub_sa_len = j - i + 1;
  let mut meas_4_bpa_pos_pair = vec![0.; sub_sa_len - 1];
  for n in i + 2 .. j {
    let mut mea = 0.;
    match pos_seqs_with_poss_4_forward_bpas.get(&n) {
      Some(poss) => {
        for &m in poss {
          if m <= i {continue;}
          let ea = meas_4_bpa_pos_pair[m - i - 1] + mea_mat_4_bpa_pos_pairs[&(m, n)];
          if ea > mea {
            mea = ea;
          }
        }
      },
      None => {},
    };
    let ea = meas_4_bpa_pos_pair[n - i - 1] + mean_upp_mat[n];
    if ea > mea {
      mea = ea;
    }
    meas_4_bpa_pos_pair[n - i] = mea;
  }
  meas_4_bpa_pos_pair
}

/* #[inline]
// pub fn get_mea_consensus_ss(mea_css_pair: &MeaCssPair, gamma_plus_1: Prob, bpap_mats_with_rna_id_pairs: &Prob4dMatsWithRnaIdPairs) -> MeaCss {
pub fn get_mea_consensus_ss(mea_css_pair: &MeaCssPair, gamma: Prob, bpap_mats_with_rna_id_pairs: &Prob4dMatsWithRnaIdPairs, upp_mats_with_rna_ids: &ProbSeqsWithRnaIds) -> MeaCss {
  let mea_css_pair = &if mea_css_pair.0.mea >= mea_css_pair.1.mea {*mea_css_pair} else {(mea_css_pair.1, mea_css_pair.0)};
  let mut mea_mat_4_corresponding_col_quadruples = Mea4dMat::default();
  let mut col_pair_seqs_with_col_pairs_4_forward_bpas = ColPairSeqsWithColPairs::default();
  // let inverse_gamma_plus_1 = 1. / gamma_plus_1;
  let seq_num_pair = (mea_css_pair.0.seq_num, mea_css_pair.1.seq_num);
  let sum_of_seq_num_pair = seq_num_pair.0 + seq_num_pair.1;
  let combination_num = (0 .. sum_of_seq_num_pair).combinations(2).fold(0, |acc, _| {&acc + 1}) as Prob;
  let mut mean_upps_with_cols_1 = ProbsWithCols::default();
  let mut mean_upps_with_cols_2 = mean_upps_with_cols_1.clone();
  for sub_seq_len_1 in 2 .. mea_css_pair.0.col_num + 1 {
    for i in 0 .. mea_css_pair.0.col_num - sub_seq_len_1 + 1 {
      let j = i + sub_seq_len_1 - 1;
      // if !mea_css_pair.0.rna_id_pos_triple_seqs_with_col_pairs.contains_key(&(i, j)) {continue;}
      // let ref rna_id_pos_triples_1 = mea_css_pair.0.rna_id_pos_triple_seqs_with_col_pairs[&(i, j)];
      let ref pos_pairs_1 = mea_css_pair.0.pos_seqs_with_cols[i].iter().zip(&mea_css_pair.0.pos_seqs_with_cols[j]).map(|(&a, &b)| {(a, b)}).collect::<FloatPosPairs>();
      for sub_seq_len_2 in 2 .. mea_css_pair.1.col_num + 1 {
        for k in 0 .. mea_css_pair.1.col_num - sub_seq_len_2 + 1 {
          let l = k + sub_seq_len_2 - 1;
          let col_quadruple = (i, j, k, l);
          // if !mea_css_pair.1.rna_id_pos_triple_seqs_with_col_pairs.contains_key(&(k, l)) {continue;}
          let mut mean_bpap = 0.;
          let ref pos_pairs_2 = mea_css_pair.1.pos_seqs_with_cols[k].iter().zip(&mea_css_pair.1.pos_seqs_with_cols[l]).map(|(&a, &b)| {(a, b)}).collect::<FloatPosPairs>();
          /* let ref rna_id_pos_triples_2 = mea_css_pair.1.rna_id_pos_triple_seqs_with_col_pairs[&(k, l)];
          for (m, &(rna_id_1, pos_1, pos_2)) in rna_id_pos_triples_1.iter().enumerate() {
            for &(rna_id_2, pos_3, pos_4) in &rna_id_pos_triples_1[m + 1 ..] {
              let rna_id_pair = if rna_id_1 < rna_id_2 {(rna_id_1, rna_id_2)} else {(rna_id_2, rna_id_1)};
              let pos_quadruple = if rna_id_1 < rna_id_2 {(pos_1, pos_2, pos_3, pos_4)} else {(pos_3, pos_4, pos_1, pos_2)};
              let ref bpap_mat = bpap_mats_with_rna_id_pairs[&rna_id_pair];
              if !bpap_mat.contains_key(&pos_quadruple) {continue;}
              mean_bpap += bpap_mat[&pos_quadruple];
            }
            for &(rna_id_2, pos_3, pos_4) in rna_id_pos_triples_2 {
              let rna_id_pair = if rna_id_1 < rna_id_2 {(rna_id_1, rna_id_2)} else {(rna_id_2, rna_id_1)};
              let pos_quadruple = if rna_id_1 < rna_id_2 {(pos_1, pos_2, pos_3, pos_4)} else {(pos_3, pos_4, pos_1, pos_2)};
              let ref bpap_mat = bpap_mats_with_rna_id_pairs[&rna_id_pair];
              if !bpap_mat.contains_key(&pos_quadruple) {continue;}
              mean_bpap += bpap_mat[&pos_quadruple];
            }
          }
          for (m, &(rna_id_1, pos_1, pos_2)) in rna_id_pos_triples_2.iter().enumerate() {
            for &(rna_id_2, pos_3, pos_4) in &rna_id_pos_triples_2[m + 1 ..] {
              let rna_id_pair = if rna_id_1 < rna_id_2 {(rna_id_1, rna_id_2)} else {(rna_id_2, rna_id_1)};
              let pos_quadruple = if rna_id_1 < rna_id_2 {(pos_1, pos_2, pos_3, pos_4)} else {(pos_3, pos_4, pos_1, pos_2)};
              let ref bpap_mat = bpap_mats_with_rna_id_pairs[&rna_id_pair];
              if !bpap_mat.contains_key(&pos_quadruple) {continue;}
              mean_bpap += bpap_mat[&pos_quadruple];
            }
          } */
          for (m, pos_pair_1) in pos_pairs_1.iter().enumerate() {
            if is_gap_pos(pos_pair_1.0) || is_gap_pos(pos_pair_1.1) {continue;}
            let pos_pair_1 = (pos_pair_1.0 as Pos, pos_pair_1.1 as Pos);
            let rna_id_1 = mea_css_pair.0.rna_ids[m];
            for (n, pos_pair_2) in (&pos_pairs_1[m + 1 ..]).iter().enumerate() {
              if is_gap_pos(pos_pair_2.0) || is_gap_pos(pos_pair_2.1) {continue;}
              let pos_pair_2 = (pos_pair_2.0 as Pos, pos_pair_2.1 as Pos);
              let n = n + m + 1;
              let rna_id_2 = mea_css_pair.0.rna_ids[n];
              let rna_id_pair = if rna_id_1 < rna_id_2 {(rna_id_1, rna_id_2)} else {(rna_id_2, rna_id_1)};
              let ref bpap_mat = bpap_mats_with_rna_id_pairs[&rna_id_pair];
              let pos_quadruple = if rna_id_1 < rna_id_2 {(pos_pair_1.0, pos_pair_1.1, pos_pair_2.0, pos_pair_2.1)} else {(pos_pair_2.0, pos_pair_2.1, pos_pair_1.0, pos_pair_1.1)};
              if !bpap_mat.contains_key(&pos_quadruple) {continue;}
              mean_bpap += bpap_mat[&pos_quadruple];
            }
            for (n, pos_pair_2) in pos_pairs_2.iter().enumerate() {
              if is_gap_pos(pos_pair_2.0) || is_gap_pos(pos_pair_2.1) {continue;}
              let pos_pair_2 = (pos_pair_2.0 as Pos, pos_pair_2.1 as Pos);
              let rna_id_2 = mea_css_pair.1.rna_ids[n];
              let rna_id_pair = if rna_id_1 < rna_id_2 {(rna_id_1, rna_id_2)} else {(rna_id_2, rna_id_1)};
              let ref bpap_mat = bpap_mats_with_rna_id_pairs[&rna_id_pair];
              let pos_quadruple = if rna_id_1 < rna_id_2 {(pos_pair_1.0, pos_pair_1.1, pos_pair_2.0, pos_pair_2.1)} else {(pos_pair_2.0, pos_pair_2.1, pos_pair_1.0, pos_pair_1.1)};
              if !bpap_mat.contains_key(&pos_quadruple) {continue;}
              mean_bpap += bpap_mat[&pos_quadruple];
            }
          }
          for (m, pos_pair_1) in pos_pairs_2.iter().enumerate() {
            if is_gap_pos(pos_pair_1.0) || is_gap_pos(pos_pair_1.1) {continue;}
            let pos_pair_1 = (pos_pair_1.0 as Pos, pos_pair_1.1 as Pos);
            let rna_id_1 = mea_css_pair.1.rna_ids[m];
            for (n, pos_pair_2) in (&pos_pairs_2[m + 1 ..]).iter().enumerate() {
              if is_gap_pos(pos_pair_2.0) || is_gap_pos(pos_pair_2.1) {continue;}
              let pos_pair_2 = (pos_pair_2.0 as Pos, pos_pair_2.1 as Pos);
              let n = n + m + 1;
              let rna_id_2 = mea_css_pair.1.rna_ids[n];
              let rna_id_pair = if rna_id_1 < rna_id_2 {(rna_id_1, rna_id_2)} else {(rna_id_2, rna_id_1)};
              let ref bpap_mat = bpap_mats_with_rna_id_pairs[&rna_id_pair];
              let pos_quadruple = if rna_id_1 < rna_id_2 {(pos_pair_1.0, pos_pair_1.1, pos_pair_2.0, pos_pair_2.1)} else {(pos_pair_2.0, pos_pair_2.1, pos_pair_1.0, pos_pair_1.1)};
              if !bpap_mat.contains_key(&pos_quadruple) {continue;}
              mean_bpap += bpap_mat[&pos_quadruple];
            }
          }
          mean_bpap /= combination_num;
          if mean_bpap == 0. {
            continue;
          }
          // println!("i: {}, j: {}, k: {}, l: {}.", i, j, k, l);
          let mea_mat_4_corresponding_col_quadruple = get_mea_mat_4_corresponding_col_quadruple(&col_quadruple, &mea_mat_4_corresponding_col_quadruples, &col_pair_seqs_with_col_pairs_4_forward_bpas, upp_mats_with_rna_ids, mea_css_pair, &mut mean_upps_with_cols_1, &mut mean_upps_with_cols_2);
          // mea_mat_4_corresponding_col_quadruples.insert(col_quadruple, mea_mat_4_corresponding_col_quadruple[j - i - 1][l - k - 1] + gamma_plus_1 * mean_bpap - 1.);
          mea_mat_4_corresponding_col_quadruples.insert(col_quadruple, mea_mat_4_corresponding_col_quadruple[j - i - 1][l - k - 1] + gamma * mean_bpap);
          if col_pair_seqs_with_col_pairs_4_forward_bpas.contains_key(&(j, l)) {
            col_pair_seqs_with_col_pairs_4_forward_bpas.get_mut(&(j, l)).expect("Failed to get an element of a hash map.").push((i, k));
          } else {
            col_pair_seqs_with_col_pairs_4_forward_bpas.insert((j, l), vec![(i, k)]);
          }
        }
      }
    }
  }
  // println!("Computed DP matrix.");
  let mut mea_css = MeaCss::new();
  let pseudo_col_quadruple = (0, mea_css_pair.0.col_num - 1, 0, mea_css_pair.1.col_num - 1);
  let mut col_quadruple_stack = vec![pseudo_col_quadruple];
  // let mut pos_seqs = FloatPosSeqs::new();
  // let mut pos_pair_seqs = FLoatPosPairSeqs::new();
  // let mut rna_id_pos_pair_seqs = RnaIdPosPairSeqs::new();
  // let mut pos_pairs_exist_in_fisrt_seq = BoolsWithPosPairs::default();
  while col_quadruple_stack.len() > 0 {
    let col_quadruple_1 = col_quadruple_stack.pop().expect("Failed to pop an element of a vector.");
    let (i, j, k, l) = col_quadruple_1;
    /* let first_seq_rna_id_pos_triple = mea_css_pair.0.rna_id_pos_triple_seqs_with_col_pairs[&(i, j)][0];
    let first_seq_pos_pair = (first_seq_rna_id_pos_triple.1, first_seq_rna_id_pos_triple.2);
    pos_pairs_exist_in_fisrt_seq.insert(first_seq_pos_pair, true);
    let mut left_rna_id_pos_pairs = RnaIdPosPairs::new();
    let mut right_rna_id_pos_pairs = left_rna_id_pos_pairs.clone();
    for &(rna_id, m, n) in &mea_css_pair.0.rna_id_pos_triple_seqs_with_col_pairs[&(i, j)] {
      left_rna_id_pos_pairs.push((rna_id, m));
      right_rna_id_pos_pairs.push((rna_id, n));
    }
    for &(rna_id, m, n) in &mea_css_pair.1.rna_id_pos_triple_seqs_with_col_pairs[&(k, l)] {
      left_rna_id_pos_pairs.push((rna_id, m));
      right_rna_id_pos_pairs.push((rna_id, n));
    }
    rna_id_pos_pair_seqs.push(left_rna_id_pos_pairs);
    rna_id_pos_pair_seqs.push(right_rna_id_pos_pairs); */
    /* let first_seq_pos_pair = (mea_css_pair.0.pos_seqs_with_cols[i][0], mea_css_pair.0.pos_seqs_with_cols[j][0]);
    let first_seq_pos_pair = (first_seq_pos_pair.0 as Pos, first_seq_pos_pair.1 as Pos);
    pos_pairs_exist_in_fisrt_seq.insert(first_seq_pos_pair, true); */
    let mut left_poss = mea_css_pair.0.pos_seqs_with_cols[i].clone();
    left_poss.extend(&mea_css_pair.1.pos_seqs_with_cols[k]);
    let mut right_poss = mea_css_pair.0.pos_seqs_with_cols[j].clone();
    right_poss.extend(&mea_css_pair.1.pos_seqs_with_cols[l]);
    let pos_pairs = left_poss.iter().zip(right_poss.iter()).map(|(&a, &b)| {(a, b)}).collect();
    mea_css.pos_pair_seqs.push(pos_pairs);
    mea_css.pos_seqs_with_cols.push(left_poss);
    mea_css.pos_seqs_with_cols.push(right_poss);
    let mea_mat_4_corresponding_col_quadruple = get_mea_mat_4_corresponding_col_quadruple(&col_quadruple_1, &mea_mat_4_corresponding_col_quadruples, &col_pair_seqs_with_col_pairs_4_forward_bpas, upp_mats_with_rna_ids, mea_css_pair, &mut mean_upps_with_cols_1, &mut mean_upps_with_cols_2);
    let mea = mea_mat_4_corresponding_col_quadruple[j - i - 1][l - k - 1];
    if mea == 0. {continue;}
    let mut n = j - 1;
    let mut p = l - 1;
    while n > i || p > k {
      let mea = mea_mat_4_corresponding_col_quadruple[n - i][p - k];
      if n > i && mean_upps_with_cols_1.contains_key(&n) && mea == mea_mat_4_corresponding_col_quadruple[n - i - 1][p - k] + mean_upps_with_cols_1[&n] {
        let mut poss = FloatPoss::new();
        for &m in &mea_css_pair.0.pos_seqs_with_cols[n] {
          poss.push(m);
        }
        for &o in &mea_css_pair.1.pos_seqs_with_cols[p]  {
          poss.push(if is_gap_pos(o) {o} else {o + 0.5});
        }
        mea_css.pos_seqs_with_cols.push(poss);
        n = n - 1;
      } else if p > k && mean_upps_with_cols_2.contains_key(&p) && mea == mea_mat_4_corresponding_col_quadruple[n - i][p - k - 1] + mean_upps_with_cols_2[&p] {
        let mut poss = FloatPoss::new();
        for &m in &mea_css_pair.0.pos_seqs_with_cols[n]  {
          poss.push(if is_gap_pos(m) {m} else {m + 0.5});
        }
        for &o in &mea_css_pair.1.pos_seqs_with_cols[p] {
          poss.push(o);
        }
        mea_css.pos_seqs_with_cols.push(poss);
        p = p - 1;
      } else {
        match col_pair_seqs_with_col_pairs_4_forward_bpas.get(&(n, p)) {
          Some(col_pairs) => {
            for &(m, o) in col_pairs {
              if m <= i || o <= k {continue;}
              let col_quadruple_2 = (m, n, o, p);
              if mea == mea_mat_4_corresponding_col_quadruple[m - i - 1][o - k - 1] + mea_mat_4_corresponding_col_quadruples[&col_quadruple_2] {
                col_quadruple_stack.push(col_quadruple_2);
                n = m - 1;
                p = o - 1;
                break;
              }
            }
          },
          None => {},
        }
      }
    }
  }
  // println!("Tracebacked DP matrix.");
  mea_css.col_num = mea_css.pos_seqs_with_cols.len();
  mea_css.mea = mea_mat_4_corresponding_col_quadruples[&pseudo_col_quadruple];
  mea_css.seq_num = sum_of_seq_num_pair;
  mea_css.rna_ids = mea_css_pair.0.rna_ids.clone();
  mea_css.rna_ids.extend(&mea_css_pair.1.rna_ids);
  mea_css.pos_seqs_with_cols.sort_unstable_by(|poss_1, poss_2| {poss_1.partial_cmp(&poss_2).expect("Failed to compare 2 floating-point numbers with each other.")});
  mea_css
} */

/* #[inline]
fn get_mea_mat_4_corresponding_col_quadruple(col_quadruple: &ColQuadruple, mea_mat_4_corresponding_col_quadruples: &Mea4dMat, col_pair_seqs_with_col_pairs_4_forward_bpas: &ColPairSeqsWithColPairs, upp_mats_with_rna_ids: &ProbSeqsWithRnaIds, mea_css_pair: &MeaCssPair, mean_upps_with_cols_1: &mut ProbsWithCols, mean_upps_with_cols_2: &mut ProbsWithCols) -> MeaMat {
  let &(i, j, k, l) = col_quadruple;
  let sub_seq_len_1 = j - i + 1;
  let sub_seq_len_2 = l - k + 1;
  let mut mea_mat_4_corresponding_col_quadruple = vec![vec![0.; sub_seq_len_2 - 1]; sub_seq_len_1 - 1];
  let seq_num_pair = (mea_css_pair.0.seq_num as Prob, mea_css_pair.1.seq_num as Prob);
  for n in i .. j {
    for p in k .. l {
      if n == i && p == k {
        mea_mat_4_corresponding_col_quadruple[n - i][p - k] = 0.;
        continue;
      } else if n == i {
        let mut mean_upp = 0.;
        for (&rna_id, &m) in mea_css_pair.1.rna_ids.iter().zip(mea_css_pair.1.pos_seqs_with_cols[p].iter()) {
          if is_gap_pos(m) {continue;}
          mean_upp += upp_mats_with_rna_ids[rna_id][m as Pos];
        }
        mean_upp /= seq_num_pair.1;
        if !mean_upps_with_cols_2.contains_key(&p) {
          mean_upps_with_cols_2.insert(p, mean_upp);
        }
        mea_mat_4_corresponding_col_quadruple[n - i][p - k] = mea_mat_4_corresponding_col_quadruple[n - i][p - k - 1] + mean_upp;
        continue;
      } else if p == k {
        let mut mean_upp = 0.;
        for (&rna_id, &m) in mea_css_pair.0.rna_ids.iter().zip(mea_css_pair.0.pos_seqs_with_cols[n].iter()) {
          if is_gap_pos(m) {continue;}
          mean_upp += upp_mats_with_rna_ids[rna_id][m as Pos];
        }
        mean_upp /= seq_num_pair.0;
        if !mean_upps_with_cols_1.contains_key(&n) {
          mean_upps_with_cols_1.insert(n, mean_upp);
        }
        mea_mat_4_corresponding_col_quadruple[n - i][p - k] = mea_mat_4_corresponding_col_quadruple[n - i - 1][p - k] + mean_upp;
        continue;
      }
      let mut mea = 0.;
      match col_pair_seqs_with_col_pairs_4_forward_bpas.get(&(n, p)) {
        Some(col_pairs) => {
          for &(m, o) in col_pairs {
            if m <= i || o <= k {continue;}
            let ea = mea_mat_4_corresponding_col_quadruple[m - i - 1][o - k - 1] + mea_mat_4_corresponding_col_quadruples[&(m, n, o, p)];
            if ea > mea {
              mea = ea;
            }
          }
        },
        None => {},
      }
      let mut mean_upp = 0.;
      for (&rna_id, &m) in mea_css_pair.0.rna_ids.iter().zip(mea_css_pair.0.pos_seqs_with_cols[n].iter()) {
        if is_gap_pos(m) {continue;}
        mean_upp += upp_mats_with_rna_ids[rna_id][m as Pos];
      }
      mean_upp /= seq_num_pair.0;
      if !mean_upps_with_cols_1.contains_key(&n) {
        mean_upps_with_cols_1.insert(n, mean_upp);
      }
      let ea = mea_mat_4_corresponding_col_quadruple[n - i - 1][p - k] + mean_upp;
      if ea > mea {
        mea = ea;
      }
      let mut mean_upp = 0.;
      for (&rna_id, &m) in mea_css_pair.1.rna_ids.iter().zip(mea_css_pair.1.pos_seqs_with_cols[p].iter()) {
        if is_gap_pos(m) {continue;}
        mean_upp += upp_mats_with_rna_ids[rna_id][m as Pos];
      }
      mean_upp /= seq_num_pair.1;
      if !mean_upps_with_cols_2.contains_key(&p) {
        mean_upps_with_cols_2.insert(p, mean_upp);
      }
      let ea = mea_mat_4_corresponding_col_quadruple[n - i][p - k - 1] + mean_upp;
      if ea > mea {
        mea = ea;
      }
      mea_mat_4_corresponding_col_quadruple[n - i][p - k] = mea;
    }
  }
  mea_mat_4_corresponding_col_quadruple
} */

/* #[inline]
pub fn get_guide_tree(mea_mat: &SparseMeaMat, seq_num: usize) -> GuideTree {
  let mut guide_tree = GuideTree::default();
  for _ in 0 .. seq_num {
    guide_tree.add_node(NEG_INFINITY);
  }
  let mut cluster_score_mat = ClusterScoreMat::default();
  let mut cluster_index_score_pair_seqs_with_cluster_indexes = ClusterIndexScorePairSeqsWithClusterIndexes::default();
  for i in 0 .. seq_num {
    let mut cluster_index_score_pairs = ClusterIndexScorePairs::new();
    for j in i + 1 .. seq_num {
      let mea = mea_mat[&(i, j)];
      cluster_score_mat.insert((i, j), mea);
      cluster_index_score_pairs.push(ClusterIndexScorePair::new(j, mea));
    }
    cluster_index_score_pair_seqs_with_cluster_indexes.insert(i, cluster_index_score_pairs);
  }
  for cluster_index_score_pairs in cluster_index_score_pair_seqs_with_cluster_indexes.values_mut() {
    cluster_index_score_pairs.sort_unstable_by(|cluster_index_score_pair_1, cluster_index_score_pair_2| {cluster_index_score_pair_2.score.partial_cmp(&cluster_index_score_pair_1.score).expect("Failed to compare 2 floating-point numbers with each other.")});
  }
  let mut seq_nums_with_cluster_indexes = (0 .. seq_num).map(|cluster_index| {(cluster_index, 1)}).collect::<SeqNumsWithClusterIndexes>();
  let mut new_cluster_index = seq_num;
  while seq_nums_with_cluster_indexes.len() > 1 {
    let mut cluster_index_pair_4_merge = (0, 0);
    let mut max_cluster_score = NEG_INFINITY;
    for (&i, cluster_index_score_pairs) in cluster_index_score_pair_seqs_with_cluster_indexes.iter() {
      if cluster_index_score_pairs.len() == 0 {continue;}
      let ref cluster_index_score_pair = cluster_index_score_pairs[0];
      if cluster_index_score_pair.score > max_cluster_score {
        cluster_index_pair_4_merge.0 = i;
        cluster_index_pair_4_merge.1 = cluster_index_score_pair.index;
        max_cluster_score = cluster_index_score_pair.score;
      }
    }
    let pair_of_nums_of_seqs_in_clusters = (seq_nums_with_cluster_indexes[&cluster_index_pair_4_merge.0], seq_nums_with_cluster_indexes[&cluster_index_pair_4_merge.1]);
    let sum_of_seq_num_pair = pair_of_nums_of_seqs_in_clusters.0 + pair_of_nums_of_seqs_in_clusters.1;
    seq_nums_with_cluster_indexes.remove(&cluster_index_pair_4_merge.0);
    seq_nums_with_cluster_indexes.remove(&cluster_index_pair_4_merge.1);
    for &cluster_index in seq_nums_with_cluster_indexes.keys() {
      let ordered_cluster_index_pair_1 = (min(cluster_index_pair_4_merge.0, cluster_index), max(cluster_index_pair_4_merge.0, cluster_index));
      let ordered_cluster_index_pair_2 = (min(cluster_index_pair_4_merge.1, cluster_index), max(cluster_index_pair_4_merge.1, cluster_index));
      let new_cluster_score = (pair_of_nums_of_seqs_in_clusters.0 as ClusterScore * cluster_score_mat[&ordered_cluster_index_pair_1]
      + pair_of_nums_of_seqs_in_clusters.1 as ClusterScore * cluster_score_mat[&ordered_cluster_index_pair_2])
      / sum_of_seq_num_pair as ClusterScore;
      cluster_score_mat.remove(&ordered_cluster_index_pair_1);
      cluster_score_mat.remove(&ordered_cluster_index_pair_2);
      cluster_score_mat.insert((cluster_index, new_cluster_index), new_cluster_score);
      let cluster_index_score_pairs = cluster_index_score_pair_seqs_with_cluster_indexes.get_mut(&cluster_index).expect("Failed to get an element from a hash map.");
      let mut indexs_4_remove = Vec::new();
      for (i, cluster_index_score_pair) in cluster_index_score_pairs.iter().enumerate() {
        if cluster_index_score_pair.index == cluster_index_pair_4_merge.0 || cluster_index_score_pair.index == cluster_index_pair_4_merge.1 {
          indexs_4_remove.push(i);
        }
      }
      if indexs_4_remove.len() > 0 {
        cluster_index_score_pairs.remove(indexs_4_remove[0]);
      }
      if indexs_4_remove.len() > 1 {
        cluster_index_score_pairs.remove(indexs_4_remove[1] - 1);
      }
      cluster_index_score_pairs.push(ClusterIndexScorePair::new(new_cluster_index, new_cluster_score));
      cluster_index_score_pairs.sort_unstable_by(|cluster_index_score_pair_1, cluster_index_score_pair_2| {cluster_index_score_pair_2.score.partial_cmp(&cluster_index_score_pair_1.score).expect("Failed to compare 2 floating-point numbers.")});
    }
    cluster_score_mat.remove(&cluster_index_pair_4_merge);
    cluster_index_score_pair_seqs_with_cluster_indexes.remove(&cluster_index_pair_4_merge.0);
    cluster_index_score_pair_seqs_with_cluster_indexes.remove(&cluster_index_pair_4_merge.1);
    cluster_index_score_pair_seqs_with_cluster_indexes.insert(new_cluster_index, ClusterIndexScorePairs::new());
    seq_nums_with_cluster_indexes.insert(new_cluster_index, sum_of_seq_num_pair);
    let new_node = guide_tree.add_node(max_cluster_score);
    guide_tree.add_edge(new_node, NodeIndex::new(cluster_index_pair_4_merge.0), max_cluster_score);
    guide_tree.add_edge(new_node, NodeIndex::new(cluster_index_pair_4_merge.1), max_cluster_score);
    new_cluster_index += 1;
  }
  guide_tree
}

#[inline]
pub fn is_gap_pos(pos: FloatPos) -> bool {
  if pos.fract() != 0. {true} else {false}
} */

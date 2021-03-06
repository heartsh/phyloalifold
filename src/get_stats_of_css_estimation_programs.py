#! /usr/bin/env python

import utils
from Bio import SeqIO
import seaborn
from matplotlib import pyplot
import os
import math
from math import sqrt
import multiprocessing
import numpy

seaborn.set()
pyplot.rcParams['legend.handlelength'] = 0
pyplot.rcParams['legend.fontsize'] = "x-large"
color_palette = seaborn.color_palette()
min_gamma = -4
max_gamma = 10
white = "#F2F2F2"

def main():
  (current_work_dir_path, asset_dir_path, program_dir_path, conda_program_dir_path) = utils.get_dir_paths()
  num_of_threads = multiprocessing.cpu_count()
  mafft_plus_consalifold_ppvs = []
  mafft_plus_consalifold_senss = []
  mafft_plus_consalifold_fprs = []
  mafft_plus_consalifold_f1_scores = []
  mafft_plus_consalifold_mccs = []
  probcons_plus_consalifold_ppvs = []
  probcons_plus_consalifold_senss = []
  probcons_plus_consalifold_fprs = []
  probcons_plus_consalifold_f1_scores = []
  probcons_plus_consalifold_mccs = []
  posterior_probcons_plus_consalifold_ppvs = []
  posterior_probcons_plus_consalifold_senss = []
  posterior_probcons_plus_consalifold_fprs = []
  posterior_probcons_plus_consalifold_f1_scores = []
  posterior_probcons_plus_consalifold_mccs = []
  clustalw_plus_consalifold_ppvs = []
  clustalw_plus_consalifold_senss = []
  clustalw_plus_consalifold_fprs = []
  clustalw_plus_consalifold_f1_scores = []
  clustalw_plus_consalifold_mccs = []
  mafft_xinsi_plus_consalifold_ppvs = []
  mafft_xinsi_plus_consalifold_senss = []
  mafft_xinsi_plus_consalifold_fprs = []
  mafft_xinsi_plus_consalifold_f1_scores = []
  mafft_xinsi_plus_consalifold_mccs = []
  ref_sa_plus_consalifold_ppvs = []
  ref_sa_plus_consalifold_senss = []
  ref_sa_plus_consalifold_fprs = []
  ref_sa_plus_consalifold_f1_scores = []
  ref_sa_plus_consalifold_mccs = []
  mafft_plus_centroidalifold_ppvs = []
  mafft_plus_centroidalifold_senss = []
  mafft_plus_centroidalifold_fprs = []
  mafft_plus_centroidalifold_f1_scores = []
  mafft_plus_centroidalifold_mccs = []
  probcons_plus_centroidalifold_ppvs = []
  probcons_plus_centroidalifold_senss = []
  probcons_plus_centroidalifold_fprs = []
  probcons_plus_centroidalifold_f1_scores = []
  probcons_plus_centroidalifold_mccs = []
  clustalw_plus_centroidalifold_ppvs = []
  clustalw_plus_centroidalifold_senss = []
  clustalw_plus_centroidalifold_fprs = []
  clustalw_plus_centroidalifold_f1_scores = []
  clustalw_plus_centroidalifold_mccs = []
  mafft_xinsi_plus_centroidalifold_ppvs = []
  mafft_xinsi_plus_centroidalifold_senss = []
  mafft_xinsi_plus_centroidalifold_fprs = []
  mafft_xinsi_plus_centroidalifold_f1_scores = []
  mafft_xinsi_plus_centroidalifold_mccs = []
  ref_sa_plus_centroidalifold_ppvs = []
  ref_sa_plus_centroidalifold_senss = []
  ref_sa_plus_centroidalifold_fprs = []
  ref_sa_plus_centroidalifold_f1_scores = []
  ref_sa_plus_centroidalifold_mccs = []
  mafft_plus_petfold_ppvs = []
  mafft_plus_petfold_senss = []
  mafft_plus_petfold_fprs = []
  mafft_plus_petfold_f1_scores = []
  mafft_plus_petfold_mccs = []
  probcons_plus_petfold_ppvs = []
  probcons_plus_petfold_senss = []
  probcons_plus_petfold_fprs = []
  probcons_plus_petfold_f1_scores = []
  probcons_plus_petfold_mccs = []
  clustalw_plus_petfold_ppvs = []
  clustalw_plus_petfold_senss = []
  clustalw_plus_petfold_fprs = []
  clustalw_plus_petfold_f1_scores = []
  clustalw_plus_petfold_mccs = []
  mafft_xinsi_plus_petfold_ppvs = []
  mafft_xinsi_plus_petfold_senss = []
  mafft_xinsi_plus_petfold_fprs = []
  mafft_xinsi_plus_petfold_f1_scores = []
  mafft_xinsi_plus_petfold_mccs = []
  ref_sa_plus_petfold_ppvs = []
  ref_sa_plus_petfold_senss = []
  ref_sa_plus_petfold_fprs = []
  ref_sa_plus_petfold_f1_scores = []
  ref_sa_plus_petfold_mccs = []
  mafft_plus_rnaalifold_ppv = mafft_plus_rnaalifold_sens = mafft_plus_rnaalifold_fpr = mafft_plus_rnaalifold_f1_score = mafft_plus_rnaalifold_mcc = 0.
  probcons_plus_rnaalifold_ppv = probcons_plus_rnaalifold_sens = probcons_plus_rnaalifold_fpr = probcons_plus_rnaalifold_f1_score = probcons_plus_rnaalifold_mcc = 0.
  clustalw_plus_rnaalifold_ppv = clustalw_plus_rnaalifold_sens = clustalw_plus_rnaalifold_fpr = clustalw_plus_rnaalifold_f1_score = clustalw_plus_rnaalifold_mcc = 0.
  mafft_xinsi_plus_rnaalifold_ppv = mafft_xinsi_plus_rnaalifold_sens = mafft_xinsi_plus_rnaalifold_fpr = mafft_xinsi_plus_rnaalifold_f1_score = mafft_xinsi_plus_rnaalifold_mcc = 0.
  ref_sa_plus_rnaalifold_ppv = ref_sa_plus_rnaalifold_sens = ref_sa_plus_rnaalifold_fpr = ref_sa_plus_rnaalifold_f1_score = ref_sa_plus_rnaalifold_mcc = 0.
  gammas = [2. ** i for i in range(min_gamma, max_gamma + 1)]
  rna_fam_dir_path = asset_dir_path + "/compiled_rna_fams"
  # rna_fam_dir_path = asset_dir_path + "/compiled_rna_fams_4_micro_bench"
  ref_sa_dir_path = asset_dir_path + "/ref_sas"
  # ref_sa_dir_path = asset_dir_path + "/ref_sas_4_micro_bench"
  mafft_plus_consalifold_css_dir_path = asset_dir_path + "/mafft_plus_consalifold"
  probcons_plus_consalifold_css_dir_path = asset_dir_path + "/probcons_plus_consalifold"
  posterior_probcons_plus_consalifold_css_dir_path = asset_dir_path + "/posterior_probcons_plus_consalifold"
  clustalw_plus_consalifold_css_dir_path = asset_dir_path + "/clustalw_plus_consalifold"
  mafft_xinsi_plus_consalifold_css_dir_path = asset_dir_path + "/mafft_xinsi_plus_consalifold"
  ref_sa_plus_consalifold_css_dir_path = asset_dir_path + "/ref_sa_plus_consalifold"
  mafft_plus_centroidalifold_css_dir_path = asset_dir_path + "/mafft_plus_centroidalifold"
  probcons_plus_centroidalifold_css_dir_path = asset_dir_path + "/probcons_plus_centroidalifold"
  clustalw_plus_centroidalifold_css_dir_path = asset_dir_path + "/clustalw_plus_centroidalifold"
  mafft_xinsi_plus_centroidalifold_css_dir_path = asset_dir_path + "/mafft_xinsi_plus_centroidalifold"
  ref_sa_plus_centroidalifold_css_dir_path = asset_dir_path + "/ref_sa_plus_centroidalifold"
  mafft_plus_rnaalifold_css_dir_path = asset_dir_path + "/mafft_plus_rnaalifold"
  probcons_plus_rnaalifold_css_dir_path = asset_dir_path + "/probcons_plus_rnaalifold"
  clustalw_plus_rnaalifold_css_dir_path = asset_dir_path + "/clustalw_plus_rnaalifold"
  mafft_xinsi_plus_rnaalifold_css_dir_path = asset_dir_path + "/mafft_xinsi_plus_rnaalifold"
  ref_sa_plus_rnaalifold_css_dir_path = asset_dir_path + "/ref_sa_plus_rnaalifold"
  mafft_plus_petfold_css_dir_path = asset_dir_path + "/mafft_plus_petfold"
  probcons_plus_petfold_css_dir_path = asset_dir_path + "/probcons_plus_petfold"
  clustalw_plus_petfold_css_dir_path = asset_dir_path + "/clustalw_plus_petfold"
  mafft_xinsi_plus_petfold_css_dir_path = asset_dir_path + "/mafft_xinsi_plus_petfold"
  ref_sa_plus_petfold_css_dir_path = asset_dir_path + "/ref_sa_plus_petfold"
  pool = multiprocessing.Pool(num_of_threads)
  for gamma in gammas:
    mafft_plus_consalifold_count_params = []
    probcons_plus_consalifold_count_params = []
    posterior_probcons_plus_consalifold_count_params = []
    clustalw_plus_consalifold_count_params = []
    mafft_xinsi_plus_consalifold_count_params = []
    ref_sa_plus_consalifold_count_params = []
    mafft_plus_centroidalifold_count_params = []
    probcons_plus_centroidalifold_count_params = []
    clustalw_plus_centroidalifold_count_params = []
    mafft_xinsi_plus_centroidalifold_count_params = []
    ref_sa_plus_centroidalifold_count_params = []
    mafft_plus_petfold_count_params = []
    probcons_plus_petfold_count_params = []
    clustalw_plus_petfold_count_params = []
    mafft_xinsi_plus_petfold_count_params = []
    ref_sa_plus_petfold_count_params = []
    mafft_plus_rnaalifold_count_params = []
    probcons_plus_rnaalifold_count_params = []
    clustalw_plus_rnaalifold_count_params = []
    mafft_xinsi_plus_rnaalifold_count_params = []
    ref_sa_plus_rnaalifold_count_params = []
    gamma_str = str(gamma) if gamma < 1 else str(int(gamma))
    for rna_fam_file in os.listdir(rna_fam_dir_path):
      if not rna_fam_file.endswith(".fa"):
        continue
      rna_seq_file_path = os.path.join(rna_fam_dir_path, rna_fam_file)
      rna_seq_lens = [len(rna_seq.seq) for rna_seq in SeqIO.parse(rna_seq_file_path, "fasta")]
      num_of_rnas = len(rna_seq_lens)
      (rna_fam_name, extension) = os.path.splitext(rna_fam_file)
      ref_css_file_path = os.path.join(ref_sa_dir_path, rna_fam_name + ".sth")
      ref_css, ref_flat_css, ref_col_css, ref_flat_col_css, _, _, sta = utils.get_css_and_flat_css(ref_css_file_path)
      sta_len = len(sta[0])
      ref_csss_and_flat_csss = (ref_css, ref_flat_css, ref_col_css, ref_flat_col_css)
      mafft_plus_consalifold_estimated_css_dir_path = os.path.join(mafft_plus_consalifold_css_dir_path, rna_fam_name)
      probcons_plus_consalifold_estimated_css_dir_path = os.path.join(probcons_plus_consalifold_css_dir_path, rna_fam_name)
      posterior_probcons_plus_consalifold_estimated_css_dir_path = os.path.join(posterior_probcons_plus_consalifold_css_dir_path, rna_fam_name)
      clustalw_plus_consalifold_estimated_css_dir_path = os.path.join(clustalw_plus_consalifold_css_dir_path, rna_fam_name)
      mafft_xinsi_plus_consalifold_estimated_css_dir_path = os.path.join(mafft_xinsi_plus_consalifold_css_dir_path, rna_fam_name)
      ref_sa_plus_consalifold_estimated_css_dir_path = os.path.join(ref_sa_plus_consalifold_css_dir_path, rna_fam_name)
      mafft_plus_centroidalifold_estimated_css_dir_path = os.path.join(mafft_plus_centroidalifold_css_dir_path, rna_fam_name)
      probcons_plus_centroidalifold_estimated_css_dir_path = os.path.join(probcons_plus_centroidalifold_css_dir_path, rna_fam_name)
      clustalw_plus_centroidalifold_estimated_css_dir_path = os.path.join(clustalw_plus_centroidalifold_css_dir_path, rna_fam_name)
      mafft_xinsi_plus_centroidalifold_estimated_css_dir_path = os.path.join(mafft_xinsi_plus_centroidalifold_css_dir_path, rna_fam_name)
      ref_sa_plus_centroidalifold_estimated_css_dir_path = os.path.join(ref_sa_plus_centroidalifold_css_dir_path, rna_fam_name)
      mafft_plus_petfold_estimated_css_dir_path = os.path.join(mafft_plus_petfold_css_dir_path, rna_fam_name)
      probcons_plus_petfold_estimated_css_dir_path = os.path.join(probcons_plus_petfold_css_dir_path, rna_fam_name)
      clustalw_plus_petfold_estimated_css_dir_path = os.path.join(clustalw_plus_petfold_css_dir_path, rna_fam_name)
      mafft_xinsi_plus_petfold_estimated_css_dir_path = os.path.join(mafft_xinsi_plus_petfold_css_dir_path, rna_fam_name)
      ref_sa_plus_petfold_estimated_css_dir_path = os.path.join(ref_sa_plus_petfold_css_dir_path, rna_fam_name)
      mafft_plus_consalifold_estimated_css_file_path = os.path.join(mafft_plus_consalifold_estimated_css_dir_path, "gamma=" + gamma_str + ".sth")
      estimated_css_and_flat_css = utils.get_css_and_flat_css(mafft_plus_consalifold_estimated_css_file_path)
      mafft_plus_consalifold_count_params.insert(0, (rna_seq_lens, estimated_css_and_flat_css, ref_csss_and_flat_csss, sta_len))
      probcons_plus_consalifold_estimated_css_file_path = os.path.join(probcons_plus_consalifold_estimated_css_dir_path, "gamma=" + gamma_str + ".sth")
      estimated_css_and_flat_css = utils.get_css_and_flat_css(probcons_plus_consalifold_estimated_css_file_path)
      probcons_plus_consalifold_count_params.insert(0, (rna_seq_lens, estimated_css_and_flat_css, ref_csss_and_flat_csss, sta_len))
      posterior_probcons_plus_consalifold_estimated_css_file_path = os.path.join(posterior_probcons_plus_consalifold_estimated_css_dir_path, "gamma=" + gamma_str + ".sth")
      estimated_css_and_flat_css = utils.get_css_and_flat_css(posterior_probcons_plus_consalifold_estimated_css_file_path)
      posterior_probcons_plus_consalifold_count_params.insert(0, (rna_seq_lens, estimated_css_and_flat_css, ref_csss_and_flat_csss, sta_len))
      clustalw_plus_consalifold_estimated_css_file_path = os.path.join(clustalw_plus_consalifold_estimated_css_dir_path, "gamma=" + gamma_str + ".sth")
      estimated_css_and_flat_css = utils.get_css_and_flat_css(clustalw_plus_consalifold_estimated_css_file_path)
      clustalw_plus_consalifold_count_params.insert(0, (rna_seq_lens, estimated_css_and_flat_css, ref_csss_and_flat_csss, sta_len))
      mafft_xinsi_plus_consalifold_estimated_css_file_path = os.path.join(mafft_xinsi_plus_consalifold_estimated_css_dir_path, "gamma=" + gamma_str + ".sth")
      estimated_css_and_flat_css = utils.get_css_and_flat_css(mafft_xinsi_plus_consalifold_estimated_css_file_path)
      mafft_xinsi_plus_consalifold_count_params.insert(0, (rna_seq_lens, estimated_css_and_flat_css, ref_csss_and_flat_csss, sta_len))
      ref_sa_plus_consalifold_estimated_css_file_path = os.path.join(ref_sa_plus_consalifold_estimated_css_dir_path, "gamma=" + gamma_str + ".sth")
      estimated_css_and_flat_css = utils.get_css_and_flat_css(ref_sa_plus_consalifold_estimated_css_file_path)
      ref_sa_plus_consalifold_count_params.insert(0, (rna_seq_lens, estimated_css_and_flat_css, ref_csss_and_flat_csss, sta_len))
      mafft_plus_centroidalifold_estimated_css_file_path = os.path.join(mafft_plus_centroidalifold_estimated_css_dir_path, "gamma=" + gamma_str + ".sth")
      estimated_css_and_flat_css = utils.get_css_and_flat_css(mafft_plus_centroidalifold_estimated_css_file_path)
      mafft_plus_centroidalifold_count_params.insert(0, (rna_seq_lens, estimated_css_and_flat_css, ref_csss_and_flat_csss, sta_len))
      probcons_plus_centroidalifold_estimated_css_file_path = os.path.join(probcons_plus_centroidalifold_estimated_css_dir_path, "gamma=" + gamma_str + ".sth")
      estimated_css_and_flat_css = utils.get_css_and_flat_css(probcons_plus_centroidalifold_estimated_css_file_path)
      probcons_plus_centroidalifold_count_params.insert(0, (rna_seq_lens, estimated_css_and_flat_css, ref_csss_and_flat_csss, sta_len))
      clustalw_plus_centroidalifold_estimated_css_file_path = os.path.join(clustalw_plus_centroidalifold_estimated_css_dir_path, "gamma=" + gamma_str + ".sth")
      estimated_css_and_flat_css = utils.get_css_and_flat_css(clustalw_plus_centroidalifold_estimated_css_file_path)
      clustalw_plus_centroidalifold_count_params.insert(0, (rna_seq_lens, estimated_css_and_flat_css, ref_csss_and_flat_csss, sta_len))
      mafft_xinsi_plus_centroidalifold_estimated_css_file_path = os.path.join(mafft_xinsi_plus_centroidalifold_estimated_css_dir_path, "gamma=" + gamma_str + ".sth")
      estimated_css_and_flat_css = utils.get_css_and_flat_css(mafft_xinsi_plus_centroidalifold_estimated_css_file_path)
      mafft_xinsi_plus_centroidalifold_count_params.insert(0, (rna_seq_lens, estimated_css_and_flat_css, ref_csss_and_flat_csss, sta_len))
      ref_sa_plus_centroidalifold_estimated_css_file_path = os.path.join(ref_sa_plus_centroidalifold_estimated_css_dir_path, "gamma=" + gamma_str + ".sth")
      estimated_css_and_flat_css = utils.get_css_and_flat_css(ref_sa_plus_centroidalifold_estimated_css_file_path)
      ref_sa_plus_centroidalifold_count_params.insert(0, (rna_seq_lens, estimated_css_and_flat_css, ref_csss_and_flat_csss, sta_len))
      mafft_plus_petfold_estimated_css_file_path = os.path.join(mafft_plus_petfold_estimated_css_dir_path, "gamma=" + gamma_str + ".sth")
      estimated_css_and_flat_css = utils.get_css_and_flat_css(mafft_plus_petfold_estimated_css_file_path)
      mafft_plus_petfold_count_params.insert(0, (rna_seq_lens, estimated_css_and_flat_css, ref_csss_and_flat_csss, sta_len))
      probcons_plus_petfold_estimated_css_file_path = os.path.join(probcons_plus_petfold_estimated_css_dir_path, "gamma=" + gamma_str + ".sth")
      estimated_css_and_flat_css = utils.get_css_and_flat_css(probcons_plus_petfold_estimated_css_file_path)
      probcons_plus_petfold_count_params.insert(0, (rna_seq_lens, estimated_css_and_flat_css, ref_csss_and_flat_csss, sta_len))
      clustalw_plus_petfold_estimated_css_file_path = os.path.join(clustalw_plus_petfold_estimated_css_dir_path, "gamma=" + gamma_str + ".sth")
      estimated_css_and_flat_css = utils.get_css_and_flat_css(clustalw_plus_petfold_estimated_css_file_path)
      clustalw_plus_petfold_count_params.insert(0, (rna_seq_lens, estimated_css_and_flat_css, ref_csss_and_flat_csss, sta_len))
      mafft_xinsi_plus_petfold_estimated_css_file_path = os.path.join(mafft_xinsi_plus_petfold_estimated_css_dir_path, "gamma=" + gamma_str + ".sth")
      estimated_css_and_flat_css = utils.get_css_and_flat_css(mafft_xinsi_plus_petfold_estimated_css_file_path)
      mafft_xinsi_plus_petfold_count_params.insert(0, (rna_seq_lens, estimated_css_and_flat_css, ref_csss_and_flat_csss, sta_len))
      ref_sa_plus_petfold_estimated_css_file_path = os.path.join(ref_sa_plus_petfold_estimated_css_dir_path, "gamma=" + gamma_str + ".sth")
      estimated_css_and_flat_css = utils.get_css_and_flat_css(ref_sa_plus_petfold_estimated_css_file_path)
      ref_sa_plus_petfold_count_params.insert(0, (rna_seq_lens, estimated_css_and_flat_css, ref_csss_and_flat_csss, sta_len))
      if gamma == 1.:
        mafft_plus_rnaalifold_estimated_css_file_path = os.path.join(mafft_plus_rnaalifold_css_dir_path, rna_fam_name + ".sth")
        estimated_css_and_flat_css = utils.get_css_and_flat_css(mafft_plus_rnaalifold_estimated_css_file_path)
        mafft_plus_rnaalifold_count_params.insert(0, (rna_seq_lens, estimated_css_and_flat_css, ref_csss_and_flat_csss, sta_len))
        probcons_plus_rnaalifold_estimated_css_file_path = os.path.join(probcons_plus_rnaalifold_css_dir_path, rna_fam_name + ".sth")
        estimated_css_and_flat_css = utils.get_css_and_flat_css(probcons_plus_rnaalifold_estimated_css_file_path)
        probcons_plus_rnaalifold_count_params.insert(0, (rna_seq_lens, estimated_css_and_flat_css, ref_csss_and_flat_csss, sta_len))
        clustalw_plus_rnaalifold_estimated_css_file_path = os.path.join(clustalw_plus_rnaalifold_css_dir_path, rna_fam_name + ".sth")
        estimated_css_and_flat_css = utils.get_css_and_flat_css(clustalw_plus_rnaalifold_estimated_css_file_path)
        clustalw_plus_rnaalifold_count_params.insert(0, (rna_seq_lens, estimated_css_and_flat_css, ref_csss_and_flat_csss, sta_len))
        mafft_xinsi_plus_rnaalifold_estimated_css_file_path = os.path.join(mafft_xinsi_plus_rnaalifold_css_dir_path, rna_fam_name + ".sth")
        estimated_css_and_flat_css = utils.get_css_and_flat_css(mafft_xinsi_plus_rnaalifold_estimated_css_file_path)
        mafft_xinsi_plus_rnaalifold_count_params.insert(0, (rna_seq_lens, estimated_css_and_flat_css, ref_csss_and_flat_csss, sta_len))
        ref_sa_plus_rnaalifold_estimated_css_file_path = os.path.join(ref_sa_plus_rnaalifold_css_dir_path, rna_fam_name + ".sth")
        estimated_css_and_flat_css = utils.get_css_and_flat_css(ref_sa_plus_rnaalifold_estimated_css_file_path)
        ref_sa_plus_rnaalifold_count_params.insert(0, (rna_seq_lens, estimated_css_and_flat_css, ref_csss_and_flat_csss, sta_len))
    results = pool.map(get_bin_counts, mafft_plus_consalifold_count_params)
    ppv, sens, fpr, f1_score, mcc, col_ppv, col_sens, col_fpr, col_f1_score, col_mcc, = get_metrics(final_sum(results))
    mafft_plus_consalifold_ppvs.insert(0, ppv)
    mafft_plus_consalifold_senss.insert(0, sens)
    mafft_plus_consalifold_fprs.insert(0, fpr)
    mafft_plus_consalifold_f1_scores.append(f1_score)
    mafft_plus_consalifold_mccs.append(mcc)
    results = pool.map(get_bin_counts, probcons_plus_consalifold_count_params)
    ppv, sens, fpr, f1_score, mcc, col_ppv, col_sens, col_fpr, col_f1_score, col_mcc, = get_metrics(final_sum(results))
    probcons_plus_consalifold_ppvs.insert(0, ppv)
    probcons_plus_consalifold_senss.insert(0, sens)
    probcons_plus_consalifold_fprs.insert(0, fpr)
    probcons_plus_consalifold_f1_scores.append(f1_score)
    probcons_plus_consalifold_mccs.append(mcc)
    results = pool.map(get_bin_counts, posterior_probcons_plus_consalifold_count_params)
    ppv, sens, fpr, f1_score, mcc, col_ppv, col_sens, col_fpr, col_f1_score, col_mcc, = get_metrics(final_sum(results))
    posterior_probcons_plus_consalifold_ppvs.insert(0, ppv)
    posterior_probcons_plus_consalifold_senss.insert(0, sens)
    posterior_probcons_plus_consalifold_fprs.insert(0, fpr)
    posterior_probcons_plus_consalifold_f1_scores.append(f1_score)
    posterior_probcons_plus_consalifold_mccs.append(mcc)
    results = pool.map(get_bin_counts, clustalw_plus_consalifold_count_params)
    ppv, sens, fpr, f1_score, mcc, col_ppv, col_sens, col_fpr, col_f1_score, col_mcc, = get_metrics(final_sum(results))
    clustalw_plus_consalifold_ppvs.insert(0, ppv)
    clustalw_plus_consalifold_senss.insert(0, sens)
    clustalw_plus_consalifold_fprs.insert(0, fpr)
    clustalw_plus_consalifold_f1_scores.append(f1_score)
    clustalw_plus_consalifold_mccs.append(mcc)
    results = pool.map(get_bin_counts, mafft_xinsi_plus_consalifold_count_params)
    ppv, sens, fpr, f1_score, mcc, col_ppv, col_sens, col_fpr, col_f1_score, col_mcc, = get_metrics(final_sum(results))
    mafft_xinsi_plus_consalifold_ppvs.insert(0, ppv)
    mafft_xinsi_plus_consalifold_senss.insert(0, sens)
    mafft_xinsi_plus_consalifold_fprs.insert(0, fpr)
    mafft_xinsi_plus_consalifold_f1_scores.append(f1_score)
    mafft_xinsi_plus_consalifold_mccs.append(mcc)
    results = pool.map(get_bin_counts, ref_sa_plus_consalifold_count_params)
    ppv, sens, fpr, f1_score, mcc, col_ppv, col_sens, col_fpr, col_f1_score, col_mcc, = get_metrics(final_sum(results))
    ref_sa_plus_consalifold_ppvs.insert(0, ppv)
    ref_sa_plus_consalifold_senss.insert(0, sens)
    ref_sa_plus_consalifold_fprs.insert(0, fpr)
    ref_sa_plus_consalifold_f1_scores.append(f1_score)
    ref_sa_plus_consalifold_mccs.append(mcc)
    results = pool.map(get_bin_counts, mafft_plus_centroidalifold_count_params)
    ppv, sens, fpr, f1_score, mcc, col_ppv, col_sens, col_fpr, col_f1_score, col_mcc, = get_metrics(final_sum(results))
    mafft_plus_centroidalifold_ppvs.insert(0, ppv)
    mafft_plus_centroidalifold_senss.insert(0, sens)
    mafft_plus_centroidalifold_fprs.insert(0, fpr)
    mafft_plus_centroidalifold_f1_scores.append(f1_score)
    mafft_plus_centroidalifold_mccs.append(mcc)
    results = pool.map(get_bin_counts, probcons_plus_centroidalifold_count_params)
    ppv, sens, fpr, f1_score, mcc, col_ppv, col_sens, col_fpr, col_f1_score, col_mcc, = get_metrics(final_sum(results))
    probcons_plus_centroidalifold_ppvs.insert(0, ppv)
    probcons_plus_centroidalifold_senss.insert(0, sens)
    probcons_plus_centroidalifold_fprs.insert(0, fpr)
    probcons_plus_centroidalifold_f1_scores.append(f1_score)
    probcons_plus_centroidalifold_mccs.append(mcc)
    results = pool.map(get_bin_counts, clustalw_plus_centroidalifold_count_params)
    ppv, sens, fpr, f1_score, mcc, col_ppv, col_sens, col_fpr, col_f1_score, col_mcc, = get_metrics(final_sum(results))
    clustalw_plus_centroidalifold_ppvs.insert(0, ppv)
    clustalw_plus_centroidalifold_senss.insert(0, sens)
    clustalw_plus_centroidalifold_fprs.insert(0, fpr)
    clustalw_plus_centroidalifold_f1_scores.append(f1_score)
    clustalw_plus_centroidalifold_mccs.append(mcc)
    results = pool.map(get_bin_counts, mafft_xinsi_plus_centroidalifold_count_params)
    ppv, sens, fpr, f1_score, mcc, col_ppv, col_sens, col_fpr, col_f1_score, col_mcc, = get_metrics(final_sum(results))
    mafft_xinsi_plus_centroidalifold_ppvs.insert(0, ppv)
    mafft_xinsi_plus_centroidalifold_senss.insert(0, sens)
    mafft_xinsi_plus_centroidalifold_fprs.insert(0, fpr)
    mafft_xinsi_plus_centroidalifold_f1_scores.append(f1_score)
    mafft_xinsi_plus_centroidalifold_mccs.append(mcc)
    results = pool.map(get_bin_counts, ref_sa_plus_centroidalifold_count_params)
    ppv, sens, fpr, f1_score, mcc, col_ppv, col_sens, col_fpr, col_f1_score, col_mcc, = get_metrics(final_sum(results))
    ref_sa_plus_centroidalifold_ppvs.insert(0, ppv)
    ref_sa_plus_centroidalifold_senss.insert(0, sens)
    ref_sa_plus_centroidalifold_fprs.insert(0, fpr)
    ref_sa_plus_centroidalifold_f1_scores.append(f1_score)
    ref_sa_plus_centroidalifold_mccs.append(mcc)
    results = pool.map(get_bin_counts, mafft_plus_petfold_count_params)
    ppv, sens, fpr, f1_score, mcc, col_ppv, col_sens, col_fpr, col_f1_score, col_mcc, = get_metrics(final_sum(results))
    mafft_plus_petfold_ppvs.insert(0, ppv)
    mafft_plus_petfold_senss.insert(0, sens)
    mafft_plus_petfold_fprs.insert(0, fpr)
    mafft_plus_petfold_f1_scores.append(f1_score)
    mafft_plus_petfold_mccs.append(mcc)
    results = pool.map(get_bin_counts, probcons_plus_petfold_count_params)
    ppv, sens, fpr, f1_score, mcc, col_ppv, col_sens, col_fpr, col_f1_score, col_mcc, = get_metrics(final_sum(results))
    probcons_plus_petfold_ppvs.insert(0, ppv)
    probcons_plus_petfold_senss.insert(0, sens)
    probcons_plus_petfold_fprs.insert(0, fpr)
    probcons_plus_petfold_f1_scores.append(f1_score)
    probcons_plus_petfold_mccs.append(mcc)
    results = pool.map(get_bin_counts, clustalw_plus_petfold_count_params)
    ppv, sens, fpr, f1_score, mcc, col_ppv, col_sens, col_fpr, col_f1_score, col_mcc, = get_metrics(final_sum(results))
    clustalw_plus_petfold_ppvs.insert(0, ppv)
    clustalw_plus_petfold_senss.insert(0, sens)
    clustalw_plus_petfold_fprs.insert(0, fpr)
    clustalw_plus_petfold_f1_scores.append(f1_score)
    clustalw_plus_petfold_mccs.append(mcc)
    results = pool.map(get_bin_counts, mafft_xinsi_plus_petfold_count_params)
    ppv, sens, fpr, f1_score, mcc, col_ppv, col_sens, col_fpr, col_f1_score, col_mcc, = get_metrics(final_sum(results))
    mafft_xinsi_plus_petfold_ppvs.insert(0, ppv)
    mafft_xinsi_plus_petfold_senss.insert(0, sens)
    mafft_xinsi_plus_petfold_fprs.insert(0, fpr)
    mafft_xinsi_plus_petfold_f1_scores.append(f1_score)
    mafft_xinsi_plus_petfold_mccs.append(mcc)
    results = pool.map(get_bin_counts, clustalw_plus_petfold_count_params)
    ppv, sens, fpr, f1_score, mcc, col_ppv, col_sens, col_fpr, col_f1_score, col_mcc, = get_metrics(final_sum(results))
    ref_sa_plus_petfold_ppvs.insert(0, ppv)
    ref_sa_plus_petfold_senss.insert(0, sens)
    ref_sa_plus_petfold_fprs.insert(0, fpr)
    ref_sa_plus_petfold_f1_scores.append(f1_score)
    ref_sa_plus_petfold_mccs.append(mcc)
    if gamma == 1.:
      results = pool.map(get_bin_counts, mafft_plus_rnaalifold_count_params)
      mafft_plus_rnaalifold_ppv, mafft_plus_rnaalifold_sens, mafft_plus_rnaalifold_fpr, mafft_plus_rnaalifold_f1_score, mafft_plus_rnaalifold_mcc, col_mafft_plus_rnaalifold_ppv, col_mafft_plus_rnaalifold_sens, col_mafft_plus_rnaalifold_fpr, col_mafft_plus_rnaalifold_f1_score, col_mafft_plus_rnaalifold_mcc, = get_metrics(final_sum(results))
      results = pool.map(get_bin_counts, probcons_plus_rnaalifold_count_params)
      probcons_plus_rnaalifold_ppv, probcons_plus_rnaalifold_sens, probcons_plus_rnaalifold_fpr, probcons_plus_rnaalifold_f1_score, probcons_plus_rnaalifold_mcc, col_probcons_plus_rnaalifold_ppv, col_probcons_plus_rnaalifold_sens, col_probcons_plus_rnaalifold_fpr, col_probcons_plus_rnaalifold_f1_score, col_probcons_plus_rnaalifold_mcc, = get_metrics(final_sum(results))
      results = pool.map(get_bin_counts, clustalw_plus_rnaalifold_count_params)
      clustalw_plus_rnaalifold_ppv, clustalw_plus_rnaalifold_sens, clustalw_plus_rnaalifold_fpr, clustalw_plus_rnaalifold_f1_score, clustalw_plus_rnaalifold_mcc, col_clustalw_plus_rnaalifold_ppv, col_clustalw_plus_rnaalifold_sens, col_clustalw_plus_rnaalifold_fpr, col_clustalw_plus_rnaalifold_f1_score, col_clustalw_plus_rnaalifold_mcc, = get_metrics(final_sum(results))
      mafft_xinsi_plus_rnaalifold_ppv, mafft_xinsi_plus_rnaalifold_sens, mafft_xinsi_plus_rnaalifold_fpr, mafft_xinsi_plus_rnaalifold_f1_score, mafft_xinsi_plus_rnaalifold_mcc, col_mafft_xinsi_plus_rnaalifold_ppv, col_mafft_xinsi_plus_rnaalifold_sens, col_mafft_xinsi_plus_rnaalifold_fpr, col_mafft_xinsi_plus_rnaalifold_f1_score, col_mafft_xinsi_plus_rnaalifold_mcc, = get_metrics(final_sum(results))
      ref_sa_plus_rnaalifold_ppv, ref_sa_plus_rnaalifold_sens, ref_sa_plus_rnaalifold_fpr, ref_sa_plus_rnaalifold_f1_score, ref_sa_plus_rnaalifold_mcc, col_ref_sa_plus_rnaalifold_ppv, col_ref_sa_plus_rnaalifold_sens, col_ref_sa_plus_rnaalifold_fpr, col_ref_sa_plus_rnaalifold_f1_score, col_ref_sa_plus_rnaalifold_mcc, = get_metrics(final_sum(results))
  # Figure for ProbCons.
  line_1, = pyplot.plot(probcons_plus_consalifold_ppvs, probcons_plus_consalifold_senss, label = "ConsAlifold (ConsProb)", marker = "o", linestyle = "-")
  line_2, = pyplot.plot(probcons_plus_centroidalifold_ppvs, probcons_plus_centroidalifold_senss, label = "CentroidAlifold", marker = "s", linestyle = "--")
  line_3, = pyplot.plot(probcons_plus_petfold_ppvs, probcons_plus_petfold_senss, label = "PETfold", marker = "^", linestyle = "-.")
  line_4, = pyplot.plot(probcons_plus_rnaalifold_ppv, probcons_plus_rnaalifold_sens, label = "RNAalifold", marker = "v", linestyle = ":")
  line_5, = pyplot.plot(posterior_probcons_plus_consalifold_ppvs, posterior_probcons_plus_consalifold_senss, label = "ConsAlifold (LocARNA-P + our PCT)", marker = "d", linestyle = "-")
  pyplot.xlabel("Precision")
  pyplot.ylabel("Recall")
  image_dir_path = asset_dir_path + "/images"
  if not os.path.exists(image_dir_path):
    os.mkdir(image_dir_path)
  pyplot.tight_layout()
  pyplot.savefig(image_dir_path + "/pr_curves_on_css_estimation_probcons.eps", bbox_inches = "tight")
  pyplot.clf()
  # Figure for MAFFT.
  pyplot.figure()
  line_1, = pyplot.plot(mafft_plus_consalifold_ppvs, mafft_plus_consalifold_senss, label = "ConsAlifold (ConsProb)", marker = "o", linestyle = "-")
  line_2, = pyplot.plot(mafft_plus_centroidalifold_ppvs, mafft_plus_centroidalifold_senss, label = "CentroidAlifold", marker = "s", linestyle = "--")
  line_3, = pyplot.plot(mafft_plus_petfold_ppvs, mafft_plus_petfold_senss, label = "PETfold", marker = "^", linestyle = "-.")
  line_4, = pyplot.plot(mafft_plus_rnaalifold_ppv, mafft_plus_rnaalifold_sens, label = "RNAalifold", marker = "v", linestyle = ":")
  pyplot.xlabel("Precision")
  pyplot.ylabel("Recall")
  pyplot.legend(handles = [line_1, line_2, line_3, line_4], loc = "lower left")
  pyplot.tight_layout()
  pyplot.savefig(image_dir_path + "/pr_curves_on_css_estimation_mafft.eps", bbox_inches = "tight")
  pyplot.clf()
  # Figure for ClustalW.
  pyplot.figure()
  line_1, = pyplot.plot(clustalw_plus_consalifold_ppvs, clustalw_plus_consalifold_senss, label = "ConsAlifold (ConsProb)", marker = "o", linestyle = "-")
  line_2, = pyplot.plot(clustalw_plus_centroidalifold_ppvs, clustalw_plus_centroidalifold_senss, label = "CentroidAlifold", marker = "s", linestyle = "--")
  line_3, = pyplot.plot(clustalw_plus_petfold_ppvs, clustalw_plus_petfold_senss, label = "PETfold", marker = "^", linestyle = "-.")
  line_4, = pyplot.plot(clustalw_plus_rnaalifold_ppv, clustalw_plus_rnaalifold_sens, label = "RNAalifold", marker = "v", linestyle = ":")
  pyplot.xlabel("Precision")
  pyplot.ylabel("Recall")
  pyplot.legend(handles = [line_1, line_2, line_3, line_4], loc = "lower left")
  pyplot.tight_layout()
  pyplot.savefig(image_dir_path + "/pr_curves_on_css_estimation_clustalw.eps", bbox_inches = "tight")
  pyplot.clf()
  # Figure for MAFFT X-INS-i.
  pyplot.figure()
  line_1, = pyplot.plot(mafft_xinsi_plus_consalifold_ppvs, mafft_xinsi_plus_consalifold_senss, label = "ConsAlifold (ConsProb)", marker = "o", linestyle = "-")
  line_2, = pyplot.plot(mafft_xinsi_plus_centroidalifold_ppvs, mafft_xinsi_plus_centroidalifold_senss, label = "CentroidAlifold", marker = "s", linestyle = "--")
  line_3, = pyplot.plot(mafft_xinsi_plus_petfold_ppvs, mafft_xinsi_plus_petfold_senss, label = "PETfold", marker = "^", linestyle = "-.")
  line_4, = pyplot.plot(mafft_xinsi_plus_rnaalifold_ppv, mafft_xinsi_plus_rnaalifold_sens, label = "RNAalifold", marker = "v", linestyle = ":")
  pyplot.xlabel("Precision")
  pyplot.ylabel("Recall")
  pyplot.legend(handles = [line_1, line_2, line_3, line_4], loc = "lower left")
  pyplot.tight_layout()
  pyplot.savefig(image_dir_path + "/pr_curves_on_css_estimation_mafft_xinsi.eps", bbox_inches = "tight")
  pyplot.clf()
  # Figure for reference sequence alignments.
  pyplot.figure()
  line_1, = pyplot.plot(ref_sa_plus_consalifold_ppvs, ref_sa_plus_consalifold_senss, label = "ConsAlifold (ConsProb)", marker = "o", linestyle = "-")
  line_2, = pyplot.plot(ref_sa_plus_centroidalifold_ppvs, ref_sa_plus_centroidalifold_senss, label = "CentroidAlifold", marker = "s", linestyle = "--")
  line_3, = pyplot.plot(ref_sa_plus_petfold_ppvs, ref_sa_plus_petfold_senss, label = "PETfold", marker = "^", linestyle = "-.")
  line_4, = pyplot.plot(ref_sa_plus_rnaalifold_ppv, ref_sa_plus_rnaalifold_sens, label = "RNAalifold", marker = "v", linestyle = ":")
  pyplot.xlabel("Precision")
  pyplot.ylabel("Recall")
  pyplot.legend(handles = [line_1, line_2, line_3, line_4], loc = "lower left")
  pyplot.tight_layout()
  pyplot.savefig(image_dir_path + "/pr_curves_on_css_estimation_ref_sa.eps", bbox_inches = "tight")
  pyplot.clf()
  # Figure for ProbCons.
  pyplot.figure()
  line_1, = pyplot.plot(probcons_plus_consalifold_fprs, probcons_plus_consalifold_senss, label = "ConsAlifold (ConsProb)", marker = "o", linestyle = "-")
  line_2, = pyplot.plot(probcons_plus_centroidalifold_fprs, probcons_plus_centroidalifold_senss, label = "CentroidAlifold", marker = "s", linestyle = "--")
  line_3, = pyplot.plot(probcons_plus_petfold_fprs, probcons_plus_petfold_senss, label = "PETfold", marker = "^", linestyle = "-.")
  line_4, = pyplot.plot(probcons_plus_rnaalifold_fpr, probcons_plus_rnaalifold_sens, label = "RNAalifold", marker = "v", linestyle = ":")
  line_5, = pyplot.plot(posterior_probcons_plus_consalifold_fprs, posterior_probcons_plus_consalifold_senss, label = "ConsAlifold (LocARNA-P + our PCT)", marker = "d", linestyle = "-")
  pyplot.legend(handles = [line_1, line_2, line_3, line_4, line_5], loc = "lower right")
  pyplot.xlabel("Fall-out")
  pyplot.ylabel("Recall")
  pyplot.tight_layout()
  pyplot.savefig(image_dir_path + "/roc_curves_on_css_estimation_probcons.eps", bbox_inches = "tight")
  pyplot.clf()
  # Figure for MAFFT.
  pyplot.figure()
  line_1, = pyplot.plot(mafft_plus_consalifold_fprs, mafft_plus_consalifold_senss, label = "ConsAlifold (ConsProb)", marker = "o", linestyle = "-")
  line_2, = pyplot.plot(mafft_plus_centroidalifold_fprs, mafft_plus_centroidalifold_senss, label = "CentroidAlifold", marker = "s", linestyle = "--")
  line_3, = pyplot.plot(mafft_plus_petfold_fprs, mafft_plus_petfold_senss, label = "PETfold", marker = "^", linestyle = "-.")
  line_4, = pyplot.plot(mafft_plus_rnaalifold_fpr, mafft_plus_rnaalifold_sens, label = "RNAalifold", marker = "v", linestyle = ":")
  pyplot.xlabel("False-out")
  pyplot.ylabel("Recall")
  pyplot.tight_layout()
  pyplot.savefig(image_dir_path + "/roc_curves_on_css_estimation_mafft.eps", bbox_inches = "tight")
  pyplot.clf()
  # Figure for ClustalW.
  pyplot.figure()
  line_1, = pyplot.plot(clustalw_plus_consalifold_fprs, clustalw_plus_consalifold_senss, label = "ConsAlifold (ConsProb)", marker = "o", linestyle = "-")
  line_2, = pyplot.plot(clustalw_plus_centroidalifold_fprs, clustalw_plus_centroidalifold_senss, label = "CentroidAlifold", marker = "s", linestyle = "--")
  line_3, = pyplot.plot(clustalw_plus_petfold_fprs, clustalw_plus_petfold_senss, label = "PETfold", marker = "^", linestyle = "-.")
  line_4, = pyplot.plot(clustalw_plus_rnaalifold_fpr, clustalw_plus_rnaalifold_sens, label = "RNAalifold", marker = "v", linestyle = ":")
  pyplot.xlabel("Fall-out")
  pyplot.ylabel("Recall")
  pyplot.tight_layout()
  pyplot.savefig(image_dir_path + "/roc_curves_on_css_estimation_clustalw.eps", bbox_inches = "tight")
  pyplot.clf()
  # Figure for MAFFT X-INS-i.
  pyplot.figure()
  line_1, = pyplot.plot(mafft_xinsi_plus_consalifold_fprs, mafft_xinsi_plus_consalifold_senss, label = "ConsAlifold (ConsProb)", marker = "o", linestyle = "-")
  line_2, = pyplot.plot(mafft_xinsi_plus_centroidalifold_fprs, mafft_xinsi_plus_centroidalifold_senss, label = "CentroidAlifold", marker = "s", linestyle = "--")
  line_3, = pyplot.plot(mafft_xinsi_plus_petfold_fprs, mafft_xinsi_plus_petfold_senss, label = "PETfold", marker = "^", linestyle = "-.")
  line_4, = pyplot.plot(mafft_xinsi_plus_rnaalifold_fpr, mafft_xinsi_plus_rnaalifold_sens, label = "RNAalifold", marker = "v", linestyle = ":")
  pyplot.xlabel("Fall-out")
  pyplot.ylabel("Recall")
  pyplot.tight_layout()
  pyplot.savefig(image_dir_path + "/roc_curves_on_css_estimation_mafft_xinsi.eps", bbox_inches = "tight")
  pyplot.clf()
  # Figure for reference sequence alignments.
  pyplot.figure()
  line_1, = pyplot.plot(ref_sa_plus_consalifold_fprs, ref_sa_plus_consalifold_senss, label = "ConsAlifold (ConsProb)", marker = "o", linestyle = "-")
  line_2, = pyplot.plot(ref_sa_plus_centroidalifold_fprs, ref_sa_plus_centroidalifold_senss, label = "CentroidAlifold", marker = "s", linestyle = "--")
  line_3, = pyplot.plot(ref_sa_plus_petfold_fprs, ref_sa_plus_petfold_senss, label = "PETfold", marker = "^", linestyle = "-.")
  line_4, = pyplot.plot(ref_sa_plus_rnaalifold_fpr, ref_sa_plus_rnaalifold_sens, label = "RNAalifold", marker = "v", linestyle = ":")
  pyplot.xlabel("Fall-out")
  pyplot.ylabel("Recall")
  pyplot.tight_layout()
  pyplot.savefig(image_dir_path + "/roc_curves_on_css_estimation_ref_sa.eps", bbox_inches = "tight")
  pyplot.clf()
  # Figure for ProbCons.
  pyplot.rcParams['legend.fontsize'] = "large"
  gammas = [i for i in range(min_gamma, max_gamma + 1)]
  pyplot.figure()
  line_1, = pyplot.plot(gammas, probcons_plus_consalifold_f1_scores, label = "ConsAlifold (ConsProb)", marker = "o", linestyle = "-")
  line_2, = pyplot.plot(gammas, probcons_plus_centroidalifold_f1_scores, label = "CentroidAlifold", marker = "s", linestyle = "--")
  line_3, = pyplot.plot(gammas, probcons_plus_petfold_f1_scores, label = "PETfold", marker = "^", linestyle = "-.")
  line_4, = pyplot.plot(-2., probcons_plus_rnaalifold_f1_score, label = "RNAalifold", marker = "v", linestyle = ":")
  line_5, = pyplot.plot(gammas, posterior_probcons_plus_consalifold_f1_scores, label = "ConsAlifold (LocARNA-P + our PCT)", marker = "d", linestyle = "-")
  line_6, = pyplot.plot(min_gamma + numpy.argmax(probcons_plus_consalifold_f1_scores), max(probcons_plus_consalifold_f1_scores), label = "ConsAlifold (ConsProb)", marker = "o", linestyle = "-", markerfacecolor = white, markeredgecolor = color_palette[0])
  line_7, = pyplot.plot(min_gamma + numpy.argmax(probcons_plus_centroidalifold_f1_scores), max(probcons_plus_centroidalifold_f1_scores), label = "CentroidAlifold", marker = "s", linestyle = "--", markerfacecolor = white, markeredgecolor = color_palette[1])
  line_8, = pyplot.plot(min_gamma + numpy.argmax(probcons_plus_petfold_f1_scores), max(probcons_plus_petfold_f1_scores), label = "PETfold", marker = "^", linestyle = "-.", markerfacecolor = white, markeredgecolor = color_palette[2])
  line_9, = pyplot.plot(min_gamma + numpy.argmax(posterior_probcons_plus_consalifold_f1_scores), max(posterior_probcons_plus_consalifold_f1_scores), label = "ConsAlifold (LocARNA-P + our PCT)", marker = "d", linestyle = "-", markerfacecolor = white, markeredgecolor = color_palette[4])
  pyplot.legend(handles = [line_6, line_7, line_8, line_9], loc = "lower right")
  pyplot.xlabel("$\log_2 \gamma$")
  pyplot.ylabel("F1 score")
  pyplot.tight_layout()
  pyplot.savefig(image_dir_path + "/gammas_vs_f1_scores_on_css_estimation_probcons.eps", bbox_inches = "tight")
  pyplot.clf()
  # Figure for MAFFT.
  pyplot.rcParams['legend.fontsize'] = "x-large"
  pyplot.figure()
  line_1, = pyplot.plot(gammas, mafft_plus_consalifold_f1_scores, label = "ConsAlifold (ConsProb)", marker = "o", linestyle = "-")
  line_2, = pyplot.plot(gammas, mafft_plus_centroidalifold_f1_scores, label = "CentroidAlifold", marker = "s", linestyle = "--")
  line_3, = pyplot.plot(gammas, mafft_plus_petfold_f1_scores, label = "PETfold", marker = "^", linestyle = "-.")
  line_4, = pyplot.plot(-2., mafft_plus_rnaalifold_f1_score, label = "RNAalifold", marker = "v", linestyle = ":")
  line_5, = pyplot.plot(min_gamma + numpy.argmax(mafft_plus_consalifold_f1_scores), max(mafft_plus_consalifold_f1_scores), label = "ConsAlifold (ConsProb)", marker = "o", linestyle = "-", markerfacecolor = white, markeredgecolor = color_palette[0])
  line_6, = pyplot.plot(min_gamma + numpy.argmax(mafft_plus_centroidalifold_f1_scores), max(mafft_plus_centroidalifold_f1_scores), label = "CentroidAlifold", marker = "s", linestyle = "--", markerfacecolor = white, markeredgecolor = color_palette[1])
  line_7, = pyplot.plot(min_gamma + numpy.argmax(mafft_plus_petfold_f1_scores), max(mafft_plus_petfold_f1_scores), label = "PETfold", marker = "^", linestyle = "-.", markerfacecolor = white, markeredgecolor = color_palette[2])
  pyplot.legend(handles = [line_5, line_6, line_7], loc = "lower right")
  pyplot.xlabel("$\log_2 \gamma$")
  pyplot.ylabel("F1 score")
  pyplot.tight_layout()
  pyplot.savefig(image_dir_path + "/gammas_vs_f1_scores_on_css_estimation_mafft.eps", bbox_inches = "tight")
  pyplot.clf()
  # Figure for ClustalW.
  pyplot.figure()
  line_1, = pyplot.plot(gammas, clustalw_plus_consalifold_f1_scores, label = "ConsAlifold (ConsProb)", marker = "o", linestyle = "-")
  line_2, = pyplot.plot(gammas, clustalw_plus_centroidalifold_f1_scores, label = "CentroidAlifold", marker = "s", linestyle = "--")
  line_3, = pyplot.plot(gammas, clustalw_plus_petfold_f1_scores, label = "PETfold", marker = "^", linestyle = "-.")
  line_4, = pyplot.plot(-2., clustalw_plus_rnaalifold_f1_score, label = "RNAalifold", marker = "v", linestyle = ":")
  line_5, = pyplot.plot(min_gamma + numpy.argmax(clustalw_plus_consalifold_f1_scores), max(clustalw_plus_consalifold_f1_scores), label = "ConsAlifold (ConsProb)", marker = "o", linestyle = "-", markerfacecolor = white, markeredgecolor = color_palette[0])
  line_6, = pyplot.plot(min_gamma + numpy.argmax(clustalw_plus_centroidalifold_f1_scores), max(clustalw_plus_centroidalifold_f1_scores), label = "CentroidAlifold", marker = "s", linestyle = "--", markerfacecolor = white, markeredgecolor = color_palette[1])
  line_7, = pyplot.plot(min_gamma + numpy.argmax(clustalw_plus_petfold_f1_scores), max(clustalw_plus_petfold_f1_scores), label = "PETfold", marker = "^", linestyle = "-.", markerfacecolor = white, markeredgecolor = color_palette[2])
  pyplot.legend(handles = [line_5, line_6, line_7], loc = "lower right")
  pyplot.xlabel("$\log_2 \gamma$")
  pyplot.ylabel("F1 score")
  pyplot.tight_layout()
  pyplot.savefig(image_dir_path + "/gammas_vs_f1_scores_on_css_estimation_clustalw.eps", bbox_inches = "tight")
  pyplot.clf()
  # Figure for MAFFT X-INS-i.
  pyplot.figure()
  line_1, = pyplot.plot(gammas, mafft_xinsi_plus_consalifold_f1_scores, label = "ConsAlifold (ConsProb)", marker = "o", linestyle = "-")
  line_2, = pyplot.plot(gammas, mafft_xinsi_plus_centroidalifold_f1_scores, label = "CentroidAlifold", marker = "s", linestyle = "--")
  line_3, = pyplot.plot(gammas, mafft_xinsi_plus_petfold_f1_scores, label = "PETfold", marker = "^", linestyle = "-.")
  line_4, = pyplot.plot(-2., mafft_xinsi_plus_rnaalifold_f1_score, label = "RNAalifold", marker = "v", linestyle = ":")
  line_5, = pyplot.plot(min_gamma + numpy.argmax(mafft_xinsi_plus_consalifold_f1_scores), max(mafft_xinsi_plus_consalifold_f1_scores), label = "ConsAlifold (ConsProb)", marker = "o", linestyle = "-", markerfacecolor = white, markeredgecolor = color_palette[0])
  line_6, = pyplot.plot(min_gamma + numpy.argmax(mafft_xinsi_plus_centroidalifold_f1_scores), max(mafft_xinsi_plus_centroidalifold_f1_scores), label = "CentroidAlifold", marker = "s", linestyle = "--", markerfacecolor = white, markeredgecolor = color_palette[1])
  line_7, = pyplot.plot(min_gamma + numpy.argmax(mafft_xinsi_plus_petfold_f1_scores), max(mafft_xinsi_plus_petfold_f1_scores), label = "PETfold", marker = "^", linestyle = "-.", markerfacecolor = white, markeredgecolor = color_palette[2])
  pyplot.legend(handles = [line_5, line_6, line_7], loc = "lower right")
  pyplot.xlabel("$\log_2 \gamma$")
  pyplot.ylabel("F1 score")
  pyplot.tight_layout()
  pyplot.savefig(image_dir_path + "/gammas_vs_f1_scores_on_css_estimation_mafft_xinsi.eps", bbox_inches = "tight")
  pyplot.clf()
  # Figure for reference sequence alignments.
  pyplot.figure()
  line_1, = pyplot.plot(gammas, ref_sa_plus_consalifold_f1_scores, label = "ConsAlifold (ConsProb)", marker = "o", linestyle = "-")
  line_2, = pyplot.plot(gammas, ref_sa_plus_centroidalifold_f1_scores, label = "CentroidAlifold", marker = "s", linestyle = "--")
  line_3, = pyplot.plot(gammas, ref_sa_plus_petfold_f1_scores, label = "PETfold", marker = "^", linestyle = "-.")
  line_4, = pyplot.plot(-2., ref_sa_plus_rnaalifold_f1_score, label = "RNAalifold", marker = "v", linestyle = ":")
  line_5, = pyplot.plot(min_gamma + numpy.argmax(ref_sa_plus_consalifold_f1_scores), max(ref_sa_plus_consalifold_f1_scores), label = "ConsAlifold (ConsProb)", marker = "o", linestyle = "-", markerfacecolor = white, markeredgecolor = color_palette[0])
  line_6, = pyplot.plot(min_gamma + numpy.argmax(ref_sa_plus_centroidalifold_f1_scores), max(ref_sa_plus_centroidalifold_f1_scores), label = "CentroidAlifold", marker = "s", linestyle = "--", markerfacecolor = white, markeredgecolor = color_palette[1])
  line_7, = pyplot.plot(min_gamma + numpy.argmax(ref_sa_plus_petfold_f1_scores), max(ref_sa_plus_petfold_f1_scores), label = "PETfold", marker = "^", linestyle = "-.", markerfacecolor = white, markeredgecolor = color_palette[2])
  pyplot.legend(handles = [line_5, line_6, line_7], loc = "lower right")
  pyplot.xlabel("$\log_2 \gamma$")
  pyplot.ylabel("F1 score")
  pyplot.tight_layout()
  pyplot.savefig(image_dir_path + "/gammas_vs_f1_scores_on_css_estimation_ref_sa.eps", bbox_inches = "tight")
  pyplot.clf()
  # Figure for ProbCons.
  pyplot.figure()
  line_1, = pyplot.plot(gammas, probcons_plus_consalifold_mccs, label = "ConsAlifold (ConsProb)", marker = "o", linestyle = "-")
  line_2, = pyplot.plot(gammas, probcons_plus_centroidalifold_mccs, label = "CentroidAlifold", marker = "s", linestyle = "--")
  line_3, = pyplot.plot(gammas, probcons_plus_petfold_mccs, label = "PETfold", marker = "^", linestyle = "-.")
  line_4, = pyplot.plot(-2., probcons_plus_rnaalifold_mcc, label = "RNAalifold", marker = "v", linestyle = ":")
  line_5, = pyplot.plot(gammas, posterior_probcons_plus_consalifold_mccs, label = "ConsAlifold (LocARNA-P + our PCT)", marker = "d", linestyle = "-")
  line_6, = pyplot.plot(min_gamma + numpy.argmax(probcons_plus_consalifold_mccs), max(probcons_plus_consalifold_mccs), label = "ConsAlifold (ConsProb)", marker = "o", linestyle = "-", markerfacecolor = white, markeredgecolor = color_palette[0])
  line_7, = pyplot.plot(min_gamma + numpy.argmax(probcons_plus_centroidalifold_mccs), max(probcons_plus_centroidalifold_mccs), label = "CentroidAlifold", marker = "s", linestyle = "--", markerfacecolor = white, markeredgecolor = color_palette[1])
  line_8, = pyplot.plot(min_gamma + numpy.argmax(probcons_plus_petfold_mccs), max(probcons_plus_petfold_mccs), label = "PETfold", marker = "^", linestyle = "-.", markerfacecolor = white, markeredgecolor = color_palette[2])
  line_9, = pyplot.plot(min_gamma + numpy.argmax(posterior_probcons_plus_consalifold_mccs), max(posterior_probcons_plus_consalifold_mccs), label = "ConsAlifold (LocARNA-P + our PCT)", marker = "d", linestyle = "-", markerfacecolor = white, markeredgecolor = color_palette[4])
  pyplot.xlabel("$\log_2 \gamma$")
  pyplot.ylabel("Matthews correlation coefficient")
  pyplot.tight_layout()
  pyplot.savefig(image_dir_path + "/gammas_vs_mccs_on_css_estimation_probcons.eps", bbox_inches = "tight")
  pyplot.clf()
  # Figure for MAFFT.
  pyplot.figure()
  line_1, = pyplot.plot(gammas, mafft_plus_consalifold_mccs, label = "ConsAlifold (ConsProb)", marker = "o", linestyle = "-")
  line_2, = pyplot.plot(gammas, mafft_plus_centroidalifold_mccs, label = "CentroidAlifold", marker = "s", linestyle = "--")
  line_3, = pyplot.plot(gammas, mafft_plus_petfold_mccs, label = "PETfold", marker = "^", linestyle = "-.")
  line_4, = pyplot.plot(-2., mafft_plus_rnaalifold_mcc, label = "RNAalifold", marker = "v", linestyle = ":")
  line_5, = pyplot.plot(min_gamma + numpy.argmax(mafft_plus_consalifold_mccs), max(mafft_plus_consalifold_mccs), label = "ConsAlifold (ConsProb)", marker = "o", linestyle = "-", markerfacecolor = white, markeredgecolor = color_palette[0])
  line_6, = pyplot.plot(min_gamma + numpy.argmax(mafft_plus_centroidalifold_mccs), max(mafft_plus_centroidalifold_mccs), label = "CentroidAlifold", marker = "s", linestyle = "--", markerfacecolor = white, markeredgecolor = color_palette[1])
  line_7, = pyplot.plot(min_gamma + numpy.argmax(mafft_plus_petfold_mccs), max(mafft_plus_petfold_mccs), label = "PETfold", marker = "^", linestyle = "-.", markerfacecolor = white, markeredgecolor = color_palette[2])
  pyplot.xlabel("$\log_2 \gamma$")
  pyplot.ylabel("Matthews correlation coefficient")
  pyplot.tight_layout()
  pyplot.savefig(image_dir_path + "/gammas_vs_mccs_on_css_estimation_mafft.eps", bbox_inches = "tight")
  pyplot.clf()
  # Figure for ClustalW.
  pyplot.figure()
  line_1, = pyplot.plot(gammas, clustalw_plus_consalifold_mccs, label = "ConsAlifold (ConsProb)", marker = "o", linestyle = "-")
  line_2, = pyplot.plot(gammas, clustalw_plus_centroidalifold_mccs, label = "CentroidAlifold", marker = "s", linestyle = "--")
  line_3, = pyplot.plot(gammas, clustalw_plus_petfold_mccs, label = "PETfold", marker = "^", linestyle = "-.")
  line_4, = pyplot.plot(-2., clustalw_plus_rnaalifold_mcc, label = "RNAalifold", marker = "v", linestyle = ":")
  line_5, = pyplot.plot(min_gamma + numpy.argmax(clustalw_plus_consalifold_mccs), max(clustalw_plus_consalifold_mccs), label = "ConsAlifold (ConsProb)", marker = "o", linestyle = "-", markerfacecolor = white, markeredgecolor = color_palette[0])
  line_6, = pyplot.plot(min_gamma + numpy.argmax(clustalw_plus_centroidalifold_mccs), max(clustalw_plus_centroidalifold_mccs), label = "CentroidAlifold", marker = "s", linestyle = "--", markerfacecolor = white, markeredgecolor = color_palette[1])
  line_7, = pyplot.plot(min_gamma + numpy.argmax(clustalw_plus_petfold_mccs), max(clustalw_plus_petfold_mccs), label = "PETfold", marker = "^", linestyle = "-.", markerfacecolor = white, markeredgecolor = color_palette[2])
  pyplot.xlabel("$\log_2 \gamma$")
  pyplot.ylabel("Matthews correlation coefficient")
  pyplot.tight_layout()
  pyplot.savefig(image_dir_path + "/gammas_vs_mccs_on_css_estimation_clustalw.eps", bbox_inches = "tight")
  pyplot.clf()
  # Figure for MAFFT X-INS-i.
  pyplot.figure()
  line_1, = pyplot.plot(gammas, mafft_xinsi_plus_consalifold_mccs, label = "ConsAlifold (ConsProb)", marker = "o", linestyle = "-")
  line_2, = pyplot.plot(gammas, mafft_xinsi_plus_centroidalifold_mccs, label = "CentroidAlifold", marker = "s", linestyle = "--")
  line_3, = pyplot.plot(gammas, mafft_xinsi_plus_petfold_mccs, label = "PETfold", marker = "^", linestyle = "-.")
  line_4, = pyplot.plot(-2., mafft_xinsi_plus_rnaalifold_mcc, label = "RNAalifold", marker = "v", linestyle = ":")
  line_5, = pyplot.plot(min_gamma + numpy.argmax(mafft_xinsi_plus_consalifold_mccs), max(mafft_xinsi_plus_consalifold_mccs), label = "ConsAlifold (ConsProb)", marker = "o", linestyle = "-", markerfacecolor = white, markeredgecolor = color_palette[0])
  line_6, = pyplot.plot(min_gamma + numpy.argmax(mafft_xinsi_plus_centroidalifold_mccs), max(mafft_xinsi_plus_centroidalifold_mccs), label = "CentroidAlifold", marker = "s", linestyle = "--", markerfacecolor = white, markeredgecolor = color_palette[1])
  line_7, = pyplot.plot(min_gamma + numpy.argmax(mafft_xinsi_plus_petfold_mccs), max(mafft_xinsi_plus_petfold_mccs), label = "PETfold", marker = "^", linestyle = "-.", markerfacecolor = white, markeredgecolor = color_palette[2])
  pyplot.xlabel("$\log_2 \gamma$")
  pyplot.ylabel("Matthews correlation coefficient")
  pyplot.tight_layout()
  pyplot.savefig(image_dir_path + "/gammas_vs_mccs_on_css_estimation_mafft_xinsi.eps", bbox_inches = "tight")
  pyplot.clf()
  # Figure for reference sequence alignments.
  pyplot.figure()
  line_1, = pyplot.plot(gammas, ref_sa_plus_consalifold_mccs, label = "ConsAlifold (ConsProb)", marker = "o", linestyle = "-")
  line_2, = pyplot.plot(gammas, ref_sa_plus_centroidalifold_mccs, label = "CentroidAlifold", marker = "s", linestyle = "--")
  line_3, = pyplot.plot(gammas, ref_sa_plus_petfold_mccs, label = "PETfold", marker = "^", linestyle = "-.")
  line_4, = pyplot.plot(-2., ref_sa_plus_rnaalifold_mcc, label = "RNAalifold", marker = "v", linestyle = ":")
  line_5, = pyplot.plot(min_gamma + numpy.argmax(ref_sa_plus_consalifold_mccs), max(ref_sa_plus_consalifold_mccs), label = "ConsAlifold (ConsProb)", marker = "o", linestyle = "-", markerfacecolor = white, markeredgecolor = color_palette[0])
  line_6, = pyplot.plot(min_gamma + numpy.argmax(ref_sa_plus_centroidalifold_mccs), max(ref_sa_plus_centroidalifold_mccs), label = "CentroidAlifold", marker = "s", linestyle = "--", markerfacecolor = white, markeredgecolor = color_palette[1])
  line_7, = pyplot.plot(min_gamma + numpy.argmax(ref_sa_plus_petfold_mccs), max(ref_sa_plus_petfold_mccs), label = "PETfold", marker = "^", linestyle = "-.", markerfacecolor = white, markeredgecolor = color_palette[2])
  pyplot.xlabel("$\log_2 \gamma$")
  pyplot.ylabel("Matthews correlation coefficient")
  pyplot.tight_layout()
  pyplot.savefig(image_dir_path + "/gammas_vs_mccs_on_css_estimation_ref_sa.eps", bbox_inches = "tight")
  pyplot.clf()

def get_metrics(bin_counts):
  (tp, tn, fp, fn, col_tp, col_tn, col_fp, col_fn) = bin_counts
  ppv = get_ppv(tp, fp)
  sens = get_sens(tp, fn)
  fpr = get_fpr(tn, fp)
  f1_score = get_f1_score(ppv, sens)
  mcc = get_mcc(tp, tn, fp, fn)
  col_ppv = get_ppv(col_tp, col_fp)
  col_sens = get_sens(col_tp, col_fn)
  col_fpr = get_fpr(col_tn, col_fp)
  col_f1_score = get_f1_score(col_ppv, col_sens)
  col_mcc = get_mcc(col_tp, col_tn, col_fp, col_fn)
  return ppv, sens, fpr, f1_score, mcc, col_ppv, col_sens, col_fpr, col_f1_score, col_mcc

def get_bin_counts(params):
  rna_seq_lens, estimated_css_and_flat_css, ref_csss_and_flat_csss, sta_len = params
  num_of_rnas = len(rna_seq_lens)
  tp = fp = tn = fn = col_tp = col_fp = col_tn = col_fn = 0
  estimated_css, estimated_flat_css, estimated_col_css, estimated_flat_col_css, _, _, _, = estimated_css_and_flat_css
  ref_css, ref_flat_css, ref_col_css, ref_flat_col_css, = ref_csss_and_flat_csss
  for m in range(0, num_of_rnas):
    sub_estimated_css = estimated_css[m]
    sub_ref_css = ref_css[m]
    sub_estimated_flat_css = estimated_flat_css[m]
    sub_ref_flat_css = ref_flat_css[m]
    rna_seq_len_1 = rna_seq_lens[m]
    for i in range(0, rna_seq_len_1):
      for j in range(i + 1, rna_seq_len_1):
        estimated_bin = (i, j) in sub_estimated_css
        ref_bin = (i, j) in sub_ref_css
        if estimated_bin == ref_bin:
          if estimated_bin == True:
            tp += 1
          else:
            tn += 1
        else:
          if estimated_bin == True:
            fp += 1
          else:
            fn += 1
  for i in range(sta_len):
    for j in range(i + 1, sta_len):
      estimated_bin = (i, j) in estimated_col_css
      ref_bin = (i, j) in ref_col_css
      if estimated_bin == ref_bin:
        if estimated_bin == True:
          col_tp += 1
        else:
          col_tn += 1
      else:
        if estimated_bin == True:
          col_fp += 1
        else:
          col_fn += 1
  return tp, tn, fp, fn, col_tp, col_tn, col_fp, col_fn

def final_sum(results):
  final_tp = final_tn = final_fp = final_fn = col_final_tp = col_final_tn = col_final_fp = col_final_fn = 0.
  for tp, tn, fp, fn, col_tp, col_tn, col_fp, col_fn in results:
    final_tp += tp
    final_tn += tn
    final_fp += fp
    final_fn += fn
    col_final_tp += col_tp
    col_final_tn += col_tn
    col_final_fp += col_fp
    col_final_fn += col_fn
  return (final_tp, final_tn, final_fp, final_fn, col_final_tp, col_final_tn, col_final_fp, col_final_fn)

def get_f1_score(ppv, sens):
  return 2 * ppv * sens / (ppv + sens)

def get_mcc(tp, tn, fp, fn):
  return (tp * tn - fp * fn) / sqrt((tp + fp) * (tp + fn) * (tn + fp) * (tn + fn))

def get_ppv(tp, fp):
  return tp / (tp + fp)

def get_sens(tp, fn):
  return tp / (tp + fn)

def get_fpr(tn, fp):
  return fp / (tn + fp)

if __name__ == "__main__":
  main()

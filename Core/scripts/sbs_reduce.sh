# ==============================================
# Script to Reduce Project Size
# Developed and Tested by : Shashank Sharma
# 
# Instructions :
# 	1. Copy the script to `cmu_indic_kan` Folder.
# 	2. Provide executing permissions
#	
#		chmod 755 ./sbs_reduce.sh
#
# 	3. Run the script
#
#		./sbs_reduce.sh
# ==============================================

rm -r test/*
rm -r wav_nosilences/*
rm -r wav_noDRC/*
rm -r wav/*
rm -r prev_ssil/*
rm -r sptk_f0/*
rm -r ssil/*
rm -r lab/*
rm -r ccoefs/*
rm -r prompt-lab/*
rm -r prompt-utt/*
rm -r recording/*
rm -r mcep_deltas/*
rm -r mcep_sptk/*
rm -r unpruned/*
rm -r ehmm/*
rm -r v/*
rm -r pm_unfilled/*
rm -r f0/*
rm -r emu/*
cd festival
rm -r feats/*
rm -r disttabs/*
rm -r dur/*
rm -r utts_hmm/*
rm -r utts/*
find $(pwd) -empty -type d -delete
cd ..
#Find and delete all empty folders
find $(pwd) -empty -type d -delete

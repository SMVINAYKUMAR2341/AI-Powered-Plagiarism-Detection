import random

# Original list of references
references = [
"""[1] M. J. D. Rosario and J. Sareno, “Theses and Capstone Projects Plagiarism Checker using Kolmogorov Complexity Algorithm,” Walailak Journal of Science and Technology (WJST), vol. 17, no. 7, pp. 726–744, Jul. 2020, doi: https://doi.org/10.48048/wjst.2020.6498.
""",

"""[2] M. T. Martín-Valdivia, L. A. Ureña-López, and M. García-Vega, “The learning vector quantization algorithm applied to automatic text classification tasks,” Neural Networks, vol. 20, no. 6, pp. 748–756, Aug. 2007, doi: https://doi.org/10.1016/j.neunet.2006.12.005.
""",

"""[3] A. A. P. Ratna et al., “Cross-Language Plagiarism Detection System Using Latent Semantic Analysis and Learning Vector Quantization,” Algorithms, vol. 10, no. 2, p. 69, Jun. 2017, doi: https://doi.org/10.3390/a10020069.
""",
‌"""[4] J. Devlin, M.-W. Chang, K. Lee, and K. Toutanova, “BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding,” arXiv.org, Oct. 11, 2018. https://arxiv.org/abs/1810.04805
""",
"""[5] J. Muangprathub, S. Kajornkasirat, and A. Wanichsombat, “Document Plagiarism Detection Using a New Concept Similarity in Formal Concept Analysis,” Journal of Applied Mathematics, vol. 2021, pp. 1–10, Mar. 2021, doi: https://doi.org/10.1155/2021/6662984.
""",
"""[6] A. A. M. Saeed and A. Y. Taqa, “Using Retrieved Sources for Semantic and Lexical Plagiarism Detection,” Iraqi Journal of Science, pp. 4036–4052, Jun. 2023, doi: https://doi.org/10.24996/ijs.2023.64.6.41.
""",
‌"""[7] A. Saini and K. Sri, "Intrinsic Plagiarism Detection System Using and Evaluating Stylometric and Lexical Techniques," Semantic Scholar. [Online]. Available: https://www.semanticscholar.org/paper/Intrinsic-Plagiarism-Detection-System-Using-and-Saini-Sri/6a0318a53393b50796887cca089c86d83469cab8. [Accessed: Nov. 19, 2024].
""",
‌"""[8] H. El Mostafa and F. Benabbou, “A deep learning based technique for plagiarism detection: a comparative study,” IAES International Journal of Artificial Intelligence (IJ-AI), vol. 9, no. 1, p. 81, Mar. 2020, doi: https://doi.org/10.11591/ijai.v9.i1.pp81-90.
""",
"""[9] A. Sobowale, A. Esan, A. Tomilayo, B. Jooda, and A. Bolajoko, “Automatic plagiarism detection using fuzzy-logic,” Dutse Journal of Pure and Applied Sciences, vol. 9, no. 3a, pp. 312–318, Oct. 2023, doi: https://doi.org/10.4314/dujopas.v9i3a.31.
""",
"""[10] S. M. zu Eissen and B. Stein, “Intrinsic Plagiarism Detection,” Lecture Notes in Computer Science, pp. 565–569, 2006, doi: https://doi.org/10.1007/11735106_66.
""",
"""[11] D. Cougias and S. Piliero, “Using Hybrid Semantic Similarity Methods when Examining Corpora with Limited Content,” Mar. 07, 2023. https://www.researchgate.net/publication/369062558_Using_Hybrid_Semantic_Similarity_Methods_when_Examining_Corpora_with_Limited_Content
""",
"""[12] A. Barrón-Cedeño, M. Potthast, P. Rosso, and B. Stein, “Corpus and Evaluation Measures for Automatic Plagiarism Detection.,” Proceedings of the International Conference on Language Resources and Evaluation, LREC 2010, 17-23 May 2010, Valletta, Malta, Jan. 2010, Available: https://www.researchgate.net/publication/220745861_Corpus_and_Evaluation_Measures_for_Automatic_Plagiarism_Detection
""",
"""[13] H. A. Chowdhury and D. K. Bhattacharyya, “Plagiarism: Taxonomy, Tools and Detection Techniques,” Jan. 19, 2018. https://www.researchgate.net/publication/322634173_Plagiarism_Taxonomy_Tools_and_Detection_Techniques
""",
"""[14] M. Paul and S. Jamal, “An Improved SRL Based Plagiarism Detection Technique Using Sentence Ranking,” Procedia Computer Science, vol. 46, pp. 223–230, 2015, doi: https://doi.org/10.1016/j.procs.2015.02.015.
""",
"""[15] M. ZURINI, “Stylometry Metrics Selection for Creating a Model for Evaluating the Writing Style of Authors According to Their Cultural Orientation,” Informatica Economica, vol. 19, no. 3/2015, pp. 107–119, Sep. 2015, doi: https://doi.org/10.12948/issn14531305/19.3.2015.10.
""",
"""[16] Nawzt Hasan Qazan and A. - Mashhadany, “Performance Evaluation of the Plagiarism Systems A Systematic Review,” International Journal of Electrical Engineering and Intelligent Computing, vol. 1, no. 1, pp. 15–23, Dec. 2023, doi: https://doi.org/10.33387/ijeeic.v1i1.7203.
""",
"""[17] N. Meuschke and R. Stange, "HyPlag: A Hybrid pproach to Academic Plagiarism Detection," Semantic Scholar. [Online]. Available: https://www.semanticscholar.org/paper/HyPlag%3A-A-Hybrid-Approach-to-Academic-Plagiarism-Meuschke-Stange/98fd145df864d79d52fb2b10bdb80b7948920e14. [Accessed: Nov. 19, 2024].
""",
"""[18] A. Nwohiri, O. JODA, and O. Ajayi, “AI-POWERED PLAGIARISM DETECTION: LEVERAGING FORENSIC LINGUISTICS AND NATURAL LANGUAGE PROCESSING,” FUDMA JOURNAL OF SCIENCES, vol. 5, no. 3, pp. 207–218, Nov. 2021, doi: https://doi.org/10.33003/fjs-2021-0503-700.
""",
"""[19] B. Gipp, “Citation-based Plagiarism Detection – Idea, Implementation and Evaluation,” Academia.edu, Apr. 23, 2016. https://www.academia.edu/24683237/Citation_based_Plagiarism_Detection_Idea_Implementation_and_Evaluation (accessed Dec. 03, 2024).
""",
"""[20] L. Seaward and S. Matwin, “Intrinsic plagiarism detection using complexity analysis,” vol. 502, pp. 56–61, Jan. 2009, Available: https://www.researchgate.net/publication/287604345_Intrinsic_plagiarism_detection_using_complexity_analysis
""",
"""[21] G. Oberreuter, G. L’Huillier, S. A. Ríos, and J. D. Velásquez, “Approaches for Intrinsic and External Plagiarism Detection,” PAN ’11: Uncovering Plagiarism, Authorship, and Social Software Misuse, Jan. 2011, Available: https://www.researchgate.net/publication/220025847_Approaches_for_Intrinsic_and_External_Plagiarism_Detection
""",
"""[22] O. A. Resta, A. Aditya, and F. E. Purwiantono, “Plagiarism Detection in Students’ Theses Using The Cosine Similarity Method,” SinkrOn, vol. 5, no. 2, pp. 305–313, May 2021, doi: https://doi.org/10.33395/sinkron.v5i2.10909.
""",
"""[23] N. V. Son, L. T. Huong, and N. C. Thanh, “A two-phase plagiarism detection system based on multi-layer long short-term memory networks,” IAES International Journal of Artificial Intelligence (IJ-AI), vol. 10, no. 3, p. 636, Sep. 2021, doi: https://doi.org/10.11591/ijai.v10.i3.pp636-648.
""",
"""[24] A. Ali and A. Taqa, “Analytical Study of Traditional and Intelligent Textual Plagiarism Detection Approaches,” JOURNAL OF EDUCATION AND SCIENCE, vol. 31, no. 1, pp. 8–25, Mar. 2022, doi: https://doi.org/10.33899/edusj.2021.131895.1192.
""",
"""[25] N. V. Son, L. T. Huong, and N. C. Thanh, “A two-phase plagiarism detection system based on multi-layer long short-term memory networks,” IAES International Journal of Artificial Intelligence (IJ-AI), vol. 10, no. 3, p. 636, Sep. 2021, doi: https://doi.org/10.11591/ijai.v10.i3.pp636-648.
"""
"""[26] N. Reimers and I. Gurevych, “Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks,” arXiv.org, 2019. https://arxiv.org/abs/1908.10084
"""[27] M. Davoodifard, “Automatic Detection of Plagiarism in Writing,” Studies in Applied Linguistics and TESOL, vol. 21, no. 2, Jan. 2022, doi: https://doi.org/10.52214/salt.v21i2.9058.

[28] N. Meuschke and M. Schubotz, "Analyzing Mathematical Content to Detect Academic Plagiarism," Semantic Scholar. [Online]. Available: https://www.semanticscholar.org/paper/Analyzing-Mathematical-Content-to-Detect-Academic-Meuschke-Schubotz/7784ffb94feee0408efba91bf8bf40ece984fc54. [Accessed: Nov. 19, 2024].

[29] Vikas Thada and Dr Vivek Jaglan, “Comparison of Jaccard, Dice, Cosine Similarity Coefficient To Find Best Fitness Value for Web Retrieved Documents Using Genetic Algorithm,” International Journal of Innovations in Engineering and Technology, vol. 2, no. 4, pp. 202–205, Aug. 2013, Available: https://www.researchgate.net/publication/306204167_Comparison_of_Jaccard_Dice_Cosine_Similarity_Coefficient_To_Find_Best_Fitness_Value_for_Web_Retrieved_Documents_Using_Genetic_Algorithm

[30] C. Chauhan, A. Singh, M. Kumar, S. K. Singh, and A. Tiwari, “Plagiarism Checker using tf-idf, cosine similarity and jaccard similarity,” INTERNATIONAL JOURNAL OF NOVEL RESEARCH AND DEVELOPMENT, vol. 8, no. 5, pp. h667–h671h667–h671, May 2023, Accessed: Dec. 03, 2024. [Online]. Available: https://www.ijnrd.org/viewpaperforall.php?paper=IJNRD2305788
[31] Naresh E, Hemavathi P, Padmavathi S, S. N. N, and S. Mallik, “Autonomous Garbage Accumulation Robot using Internet of Things,” Journal of Machine and Computing, pp. 431–440, Apr. 2024, doi: https://doi.org/10.53759/7669/jmc202404041.

‌[32] Pramod K. B. Rangaiah, P. kumar, F. Huss, and R. Augustine, “Precision Diagnosis of Burn Injuries: Clinical Implications of Imaging and Predictive Modeling,” Aug. 30, 2024. https://www.researchgate.net/publication/384784765_Precision_Diagnosis_of_Burn_Injuries_Clinical_Implications_of_Imaging_and_Predictive_Modeling

[33] P. Kumar and M. B. Manjunatha, “Design and Development of ASL Recognition by Kinect Using Bag of Features,” Advances in Intelligent Systems and Computing, pp. 319–330, Jan. 2018, doi: https://doi.org/10.1007/978-981-10-5272-9_31.

[34] Rangaiah, Pramod and Augustine, Robin. Enhanced Glaucoma Detection Using U-Net and U-Net+ Architectures Using Deep Learning Techniques. SSRN. https://doi.org/10.2139/ssrn.4831407

[35] Pramod K.B. Rangaiah, and Robin Augustine. Improving Burn Diagnosis in Medical Image Retrieval from Grafting Burn Samples Using B-Coefficients and the CLAHE Algorithm. Biomedical Signal Processing and Control, Volume 99, 2025, 106814. https://doi.org/10.1016/j.bspc.2024.106814

[36] B. P. Pradeep Kumar and M. B. Manjunatha, “Performance Analysis of KNN, SVM and ANN Techniques for Gesture Recognition System,” Indian Journal of Science and Technology, vol. 9, no. S1, Dec. 2016, doi: https://doi.org/10.17485/ijst/2016/v9is1/111145.

[37] B. P. P. Kumar and M. B. Manjunatha, “A Hybrid Gesture Recognition Method for American Sign Language,” Indian Journal of Science and Technology, vol. 10, no. 1, Jan. 2017, doi: https://doi.org/10.17485/ijst/2017/v10i1/109389.

[38] P. Kumar, L. Shiva, E. Naresh, N. N. Srinidhi, and J. Shreyas, “Design of Chest Visual Based Image Reclamation Method Using Dual Tree Complex Wavelet Transform and Edge Preservation Smoothing Algorithm,” SN Computer Science, vol. 5, no. 4, Mar. 2024, doi: https://doi.org/10.1007/s42979-024-02742-3.

[39] E Naresh, S. V. N. Murthy, Piyush Kumar Pareek, K. T. Reddy, and P. Kumar, “DevOps Life Cycle Implementation on Real Life Scenarios,” 2024 International Conference on Knowledge Engineering and Communication Systems (ICKECS), pp. 1269–1271, Apr. 2024, doi: https://doi.org/10.1109/ICKECS61492.2024.10617200.

‌[40] H. El-Banna, A. A. El-Fattah, and Waleed Fakhr, “An efficient implementation of the 1D DCT using FPGA technology,” 11th IEEE International Conference on the Engineering of Computer-Based Systems (ECBS 2004), 24-27 May 2004, Brno, Czech Republic, vol. 2003, pp. 356–360, Jan. 2004, doi: https://doi.org/10.1109/ECBS.2004.1316719.

[41] Pramod K B Rangaiah, P. Kumar, and R. Augustine, “Histopathology-driven prostate cancer identification: A VBIR approach with CLAHE and GLCM insights,” Computers in Biology and Medicine, vol. 182, no. 7, p. 109213, Oct. 2024, doi: https://doi.org/10.1016/j.compbiomed.2024.109213.

‌[42] “Design and Implementation of Kogge Stone adder using CMOS and GDI Design: VLSI Based,” International Journal of Engineering and Advanced Technology, vol. 8, no. 6S3, pp. 2181–2182, Nov. 2019, doi: https://doi.org/10.35940/ijeat.f1422.0986s319.

[43] None Pramod K B, None Kumaraswamy H.V, P. Kumar, None Prathap C, and M. Swamy, “Design and analysis of UHF BJT feedback oscillator using linear and non-linear simulation,” Oct. 2013, doi: https://doi.org/10.1109/c2spca.2013.6749386.

‌[44] P. Kumar, Pramod Rangaiah, and R. Augustine, “Improving Liver Cancer Diagnosis: A Multifaceted Approach to Automated Liver Tumor Identification in Ultrasound Scans,” Jan. 2023, doi: https://doi.org/10.2139/ssrn.4646452.

[45]
P. Kumar, C. Venkatesan, S. a R, Balamurugan D, and Sathiyapriya V, “SPEECH-TO-TEXT TRANSFIGURATION IN LANGUAGE NUMERALS FOR PERPETUAL DEAF PATIENTS,” Apr. 07, 2023. https://www.researchgate.net/publication/370715938_SPEECH-TO-TEXT_TRANSFIGURATION_IN_LANGUAGE_NUMERALS_FOR_PERPETUAL_DEAF_PATIENTS


    # Additional references omitted for brevity
]

# Shuffle the references list
random.shuffle(references)

# Display shuffled references
references

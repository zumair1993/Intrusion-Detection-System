**Intrusion Detection System (IDS) Using Machine Learning**
**Author: Umair Zia**

**Data Loading and Combining:**

**Description:**
Load the CICIDS2017 datasets from their respective CSV files (replace "C:/CICIDS2017_dataset1.csv" and "C:/CICIDS2017_dataset2.csv" with your actual paths). If using separate datasets, combine them into a single DataFrame assuming they have the same columns.
Result: A combined DataFrame containing all network traffic flow records.
head(data1)
Result:
head(data1)
  Flow.Duration Total.Fwd.Packets Total.Backward.Packets Total.Length.of.Fwd.Packets Total.Length.of.Bwd.Packets
1             4                 2                      0                          37                           0
2        142377                46                     62                        1325                      105855
3        118873                23                     28                        1169                       45025
4        143577                43                     55                        1301                      107289
5        143745                49                     59                        1331                      110185
6        120792                 1                      1                          48                         100
  Fwd.Packet.Length.Max Fwd.Packet.Length.Min Fwd.Packet.Length.Mean Fwd.Packet.Length.Std Bwd.Packet.Length.Max
1                    31                     6               18.50000              17.67767                     0
2                   570                     0               28.80435             111.40728                  4344
3                   570                     0               50.82609             156.13737                  2896
4                   570                     0               30.25581             115.17897                  4344
5                   570                     0               27.16327             108.06718                  4344
6                    48                    48               48.00000               0.00000                   100
  Bwd.Packet.Length.Min Bwd.Packet.Length.Mean Bwd.Packet.Length.Std Flow.Bytes.s Flow.Packets.s Flow.IAT.Mean
1                     0                  0.000                0.0000  9250000.000   500000.00000         4.000
2                     0               1707.339              846.1727   752790.128      758.54948      1330.626
3                     0               1608.036              902.0274   388599.598      429.02930      2377.460
4                     0               1950.709              928.2304   756318.909      682.56058      1480.175
5                     0               1867.542              928.8619   775790.462      751.33048      1343.411
6                   100                100.000                0.0000     1225.247       16.55739    120792.000
  Flow.IAT.Std Flow.IAT.Max Flow.IAT.Min Fwd.IAT.Total Fwd.IAT.Mean Fwd.IAT.Std Fwd.IAT.Max Fwd.IAT.Min Bwd.IAT.Total
1        0.000            4            4             4        4.000       0.000           4           4             0
2     5048.983        23198            0        142377     3163.933    7552.917       23792           0        119204
3     6838.421        23435            3        118873     5403.318    9768.511       24311          49         95541
4     5316.456        23220            2        143530     3417.381    7846.824       23823           2        120357
5     5112.821        24181            2        143726     2994.292    7449.819       24248           2        120164
6        0.000       120792       120792             0        0.000       0.000           0           0             0
  Bwd.IAT.Mean Bwd.IAT.Std Bwd.IAT.Max Bwd.IAT.Min Fwd.PSH.Flags Bwd.PSH.Flags Fwd.URG.Flags Bwd.URG.Flags
1        0.000       0.000           0           0             1             0             0             0
2     1954.164    6058.842       23865           4             0             0             0             0
3     3538.556    8193.060       24168           3             0             0             0             0
4     2228.833    6441.593       23889           2             0             0             0             0
5     2071.793    6233.858       24616           2             0             0             0             0
6        0.000       0.000           0           0             0             0             0             0
  Fwd.Header.Length Bwd.Header.Length Fwd.Packets.s Bwd.Packets.s Min.Packet.Length Max.Packet.Length Packet.Length.Mean
1                40                 0  5.000000e+05      0.000000                 6                31           22.66667
2              1168              1992  3.230859e+02    435.463593                 0              4344          983.30275
3               744               904  1.934838e+02    235.545498                 0              2896          888.34615
4              1120              1768  2.994909e+02    383.069712                 0              4344         1096.86869
5              1252              1896  3.408814e+02    410.449059                 0              4344         1023.08257
6                32                32  8.278694e+00      8.278694                48               100           65.33333
  Packet.Length.Std Packet.Length.Variance FIN.Flag.Count SYN.Flag.Count RST.Flag.Count PSH.Flag.Count ACK.Flag.Count
1          14.43376               208.3333              0              1              0              0              1
2        1052.39205           1107529.0280              0              0              0              1              0
3        1028.32376           1057449.7600              0              0              0              1              0
4        1183.66531           1401063.5640              0              0              0              1              0
5        1147.95835           1317808.3730              0              0              0              1              0
6          30.02221               901.3333              0              0              0              0              0
  URG.Flag.Count CWE.Flag.Count ECE.Flag.Count Down.Up.Ratio Average.Packet.Size Avg.Fwd.Segment.Size
1              0              0              0             0             34.0000             18.50000
2              0              0              0             1            992.4074             28.80435
3              0              0              0             1            905.7647             50.82609
4              0              0              0             1           1108.0612             30.25581
5              0              0              0             1           1032.5556             27.16327
6              0              0              0             1             98.0000             48.00000
  Avg.Bwd.Segment.Size Fwd.Header.Length.1 Fwd.Avg.Bytes.Bulk Fwd.Avg.Packets.Bulk Fwd.Avg.Bulk.Rate Bwd.Avg.Bytes.Bulk
1                0.000                  40                  0                    0                 0                  0
2             1707.339                1168                  0                    0                 0                  0
3             1608.036                 744                  0                    0                 0                  0
4             1950.709                1120                  0                    0                 0                  0
5             1867.542                1252                  0                    0                 0                  0
6              100.000                  32                  0                    0                 0                  0
  Bwd.Avg.Packets.Bulk Bwd.Avg.Bulk.Rate Subflow.Fwd.Packets Subflow.Fwd.Bytes Subflow.Bwd.Packets Subflow.Bwd.Bytes
1                    0                 0                   2                37                   0                 0
2                    0                 0                  46              1325                  62            105855
3                    0                 0                  23              1169                  28             45025
4                    0                 0                  43              1301                  55            107289
5                    0                 0                  49              1331                  59            110185
6                    0                 0                   1                48                   1               100
  Init_Win_bytes_forward Init_Win_bytes_backward act_data_pkt_fwd min_seg_size_forward Active.Mean Active.Std Active.Max
1                     60                      -1                1                   20           0          0          0
2                  29200                      61               30                   20           0          0          0
3                  29200                      61                4                   32           0          0          0
4                  29200                      61               26                   20           0          0          0
5                  29200                      61               31                   20           0          0          0
6                     -1                      -1                0                   32           0          0          0
  Active.Min Idle.Mean Idle.Std Idle.Max Idle.Min  Label
1          0         0        0        0        0 BENIGN
2          0         0        0        0        0 BENIGN
3          0         0        0        0        0 BENIGN
4          0         0        0        0        0 BENIGN
5          0         0        0        0        0 BENIGN
6          0         0        0        0        0 BENIGN

head(data2)
Result:

  Flow.Duration Total.Fwd.Packets Total.Backward.Packets Total.Length.of.Fwd.Packets Total.Length.of.Bwd.Packets
1  5.416666e-07                 0           3.425573e-06                4.651163e-07                9.153974e-09
2  5.416666e-07                 0           3.425573e-06                4.651163e-07                9.153974e-09
3  4.416666e-07                 0           3.425573e-06                4.651163e-07                9.153974e-09
4  7.499999e-07                 0           3.425573e-06                4.651163e-07                9.153974e-09
5  7.249999e-07                 0           3.425573e-06                4.651163e-07                9.153974e-09
6  5.499999e-07                 0           3.425573e-06                4.651163e-07                9.153974e-09
  Fwd.Packet.Length.Max Fwd.Packet.Length.Min Fwd.Packet.Length.Mean Fwd.Packet.Length.Std Bwd.Packet.Length.Max
1          0.0002417405           0.002580645            0.001009955                     0          0.0003072197
2          0.0002417405           0.002580645            0.001009955                     0          0.0003072197
3          0.0002417405           0.002580645            0.001009955                     0          0.0003072197
4          0.0002417405           0.002580645            0.001009955                     0          0.0003072197
5          0.0002417405           0.002580645            0.001009955                     0          0.0003072197
6          0.0002417405           0.002580645            0.001009955                     0          0.0003072197
  Bwd.Packet.Length.Min Bwd.Packet.Length.Mean Bwd.Packet.Length.Std Flow.Bytes.s Flow.Packets.s Flow.IAT.Mean
1           0.002071823            0.001034394                     0            0              0  5.416666e-07
2           0.002071823            0.001034394                     0            0              0  5.416666e-07
3           0.002071823            0.001034394                     0            0              0  4.416666e-07
4           0.002071823            0.001034394                     0            0              0  7.499999e-07
5           0.002071823            0.001034394                     0            0              0  7.249999e-07
6           0.002071823            0.001034394                     0            0              0  5.499999e-07
  Flow.IAT.Std Flow.IAT.Max Flow.IAT.Min Fwd.IAT.Total Fwd.IAT.Mean Fwd.IAT.Std Fwd.IAT.Max  Fwd.IAT.Min Bwd.IAT.Total
1            0 5.416666e-07 5.499999e-07             0            0           0           0 9.999999e-08             0
2            0 5.416666e-07 5.499999e-07             0            0           0           0 9.999999e-08             0
3            0 4.416666e-07 4.499999e-07             0            0           0           0 9.999999e-08             0
4            0 7.499999e-07 7.583332e-07             0            0           0           0 9.999999e-08             0
5            0 7.249999e-07 7.333332e-07             0            0           0           0 9.999999e-08             0
6            0 5.499999e-07 5.583333e-07             0            0           0           0 9.999999e-08             0
  Bwd.IAT.Mean Bwd.IAT.Std Bwd.IAT.Max Bwd.IAT.Min Fwd.PSH.Flags Bwd.PSH.Flags Fwd.URG.Flags Bwd.URG.Flags
1            0           0           0           0             0             0             0             0
2            0           0           0           0             0             0             0             0
3            0           0           0           0             0             0             0             0
4            0           0           0           0             0             0             0             0
5            0           0           0           0             0             0             0             0
6            0           0           0           0             0             0             0             0
  Fwd.Header.Length Bwd.Header.Length Fwd.Packets.s Bwd.Packets.s Min.Packet.Length Max.Packet.Length Packet.Length.Mean
1         0.9998558          0.994592   0.006410256   0.009615385       0.004143646      0.0002417405        0.001797945
2         0.9998558          0.994592   0.006410256   0.009615385       0.004143646      0.0002417405        0.001797945
3         0.9998558          0.994592   0.008333333   0.012500000       0.004143646      0.0002417405        0.001797945
4         0.9998558          0.994592   0.004329004   0.006493506       0.004143646      0.0002417405        0.001797945
5         0.9998558          0.994592   0.004504505   0.006756757       0.004143646      0.0002417405        0.001797945
6         0.9998558          0.994592   0.006289308   0.009433962       0.004143646      0.0002417405        0.001797945
  Packet.Length.Std Packet.Length.Variance FIN.Flag.Count SYN.Flag.Count RST.Flag.Count PSH.Flag.Count ACK.Flag.Count
1                 0                      0              0              0              0              0              1
2                 0                      0              0              0              0              0              1
3                 0                      0              0              0              0              0              1
4                 0                      0              0              0              0              0              1
5                 0                      0              0              0              0              0              1
6                 0                      0              0              0              0              0              1
  URG.Flag.Count CWE.Flag.Count ECE.Flag.Count Down.Up.Ratio Average.Packet.Size Avg.Fwd.Segment.Size
1              1              0              0   0.006410256         0.002311644          0.001009955
2              1              0              0   0.006410256         0.002311644          0.001009955
3              1              0              0   0.006410256         0.002311644          0.001009955
4              1              0              0   0.006410256         0.002311644          0.001009955
5              1              0              0   0.006410256         0.002311644          0.001009955
6              1              0              0   0.006410256         0.002311644          0.001009955
  Avg.Bwd.Segment.Size Fwd.Header.Length.1 Fwd.Avg.Bytes.Bulk Fwd.Avg.Packets.Bulk Fwd.Avg.Bulk.Rate Bwd.Avg.Bytes.Bulk
1          0.001034394           0.9998558                  0                    0                 0                  0
2          0.001034394           0.9998558                  0                    0                 0                  0
3          0.001034394           0.9998558                  0                    0                 0                  0
4          0.001034394           0.9998558                  0                    0                 0                  0
5          0.001034394           0.9998558                  0                    0                 0                  0
6          0.001034394           0.9998558                  0                    0                 0                  0
  Bwd.Avg.Packets.Bulk Bwd.Avg.Bulk.Rate Subflow.Fwd.Packets Subflow.Fwd.Bytes Subflow.Bwd.Packets Subflow.Bwd.Bytes
1                    0                 0                   0      4.661882e-07        3.425573e-06      9.153974e-09
2                    0                 0                   0      4.661882e-07        3.425573e-06      9.153974e-09
3                    0                 0                   0      4.661882e-07        3.425573e-06      9.153974e-09
4                    0                 0                   0      4.661882e-07        3.425573e-06      9.153974e-09
5                    0                 0                   0      4.661882e-07        3.425573e-06      9.153974e-09
6                    0                 0                   0      4.661882e-07        3.425573e-06      9.153974e-09
  Init_Win_bytes_forward Init_Win_bytes_backward act_data_pkt_fwd min_seg_size_forward Active.Mean Active.Std Active.Max
1            0.006729126             0.003631592                0            0.9999998           0          0          0
2            0.003234863             0.003921509                0            0.9999998           0          0          0
3            0.001831055             0.003921509                0            0.9999998           0          0          0
4            0.003845215             0.003921509                0            0.9999998           0          0          0
5            0.004440308             0.003921509                0            0.9999998           0          0          0
6            0.004013062             0.013763428                0            0.9999998           0          0          0
  Active.Min Idle.Mean Idle.Std Idle.Max Idle.Min Label
1          0         0        0        0        0     0
2          0         0        0        0        0     0
3          0         0        0        0        0     0
4          0         0        0        0        0     0
5          0         0        0        0        0     0
6          0         0        0        0        0     0

**Combined Data**:
head(data)
Result:

  Flow.Duration Total.Fwd.Packets Total.Backward.Packets Total.Length.of.Fwd.Packets Total.Length.of.Bwd.Packets
1             4                 2                      0                          37                           0
2        142377                46                     62                        1325                      105855
3        118873                23                     28                        1169                       45025
4        143577                43                     55                        1301                      107289
5        143745                49                     59                        1331                      110185
6        120792                 1                      1                          48                         100
  Fwd.Packet.Length.Max Fwd.Packet.Length.Min Fwd.Packet.Length.Mean Fwd.Packet.Length.Std Bwd.Packet.Length.Max
1                    31                     6               18.50000              17.67767                     0
2                   570                     0               28.80435             111.40728                  4344
3                   570                     0               50.82609             156.13737                  2896
4                   570                     0               30.25581             115.17897                  4344
5                   570                     0               27.16327             108.06718                  4344
6                    48                    48               48.00000               0.00000                   100
  Bwd.Packet.Length.Min Bwd.Packet.Length.Mean Bwd.Packet.Length.Std Flow.Bytes.s Flow.Packets.s Flow.IAT.Mean
1                     0                  0.000                0.0000  9250000.000   500000.00000         4.000
2                     0               1707.339              846.1727   752790.128      758.54948      1330.626
3                     0               1608.036              902.0274   388599.598      429.02930      2377.460
4                     0               1950.709              928.2304   756318.909      682.56058      1480.175
5                     0               1867.542              928.8619   775790.462      751.33048      1343.411
6                   100                100.000                0.0000     1225.247       16.55739    120792.000
  Flow.IAT.Std Flow.IAT.Max Flow.IAT.Min Fwd.IAT.Total Fwd.IAT.Mean Fwd.IAT.Std Fwd.IAT.Max Fwd.IAT.Min Bwd.IAT.Total
1        0.000            4            4             4        4.000       0.000           4           4             0
2     5048.983        23198            0        142377     3163.933    7552.917       23792           0        119204
3     6838.421        23435            3        118873     5403.318    9768.511       24311          49         95541
4     5316.456        23220            2        143530     3417.381    7846.824       23823           2        120357
5     5112.821        24181            2        143726     2994.292    7449.819       24248           2        120164
6        0.000       120792       120792             0        0.000       0.000           0           0             0
  Bwd.IAT.Mean Bwd.IAT.Std Bwd.IAT.Max Bwd.IAT.Min Fwd.PSH.Flags Bwd.PSH.Flags Fwd.URG.Flags Bwd.URG.Flags
1        0.000       0.000           0           0             1             0             0             0
2     1954.164    6058.842       23865           4             0             0             0             0
3     3538.556    8193.060       24168           3             0             0             0             0
4     2228.833    6441.593       23889           2             0             0             0             0
5     2071.793    6233.858       24616           2             0             0             0             0
6        0.000       0.000           0           0             0             0             0             0
  Fwd.Header.Length Bwd.Header.Length Fwd.Packets.s Bwd.Packets.s Min.Packet.Length Max.Packet.Length Packet.Length.Mean
1                40                 0  5.000000e+05      0.000000                 6                31           22.66667
2              1168              1992  3.230859e+02    435.463593                 0              4344          983.30275
3               744               904  1.934838e+02    235.545498                 0              2896          888.34615
4              1120              1768  2.994909e+02    383.069712                 0              4344         1096.86869
5              1252              1896  3.408814e+02    410.449059                 0              4344         1023.08257
6                32                32  8.278694e+00      8.278694                48               100           65.33333
  Packet.Length.Std Packet.Length.Variance FIN.Flag.Count SYN.Flag.Count RST.Flag.Count PSH.Flag.Count ACK.Flag.Count
1          14.43376               208.3333              0              1              0              0              1
2        1052.39205           1107529.0280              0              0              0              1              0
3        1028.32376           1057449.7600              0              0              0              1              0
4        1183.66531           1401063.5640              0              0              0              1              0
5        1147.95835           1317808.3730              0              0              0              1              0
6          30.02221               901.3333              0              0              0              0              0
  URG.Flag.Count CWE.Flag.Count ECE.Flag.Count Down.Up.Ratio Average.Packet.Size Avg.Fwd.Segment.Size
1              0              0              0             0             34.0000             18.50000
2              0              0              0             1            992.4074             28.80435
3              0              0              0             1            905.7647             50.82609
4              0              0              0             1           1108.0612             30.25581
5              0              0              0             1           1032.5556             27.16327
6              0              0              0             1             98.0000             48.00000
  Avg.Bwd.Segment.Size Fwd.Header.Length.1 Fwd.Avg.Bytes.Bulk Fwd.Avg.Packets.Bulk Fwd.Avg.Bulk.Rate Bwd.Avg.Bytes.Bulk
1                0.000                  40                  0                    0                 0                  0
2             1707.339                1168                  0                    0                 0                  0
3             1608.036                 744                  0                    0                 0                  0
4             1950.709                1120                  0                    0                 0                  0
5             1867.542                1252                  0                    0                 0                  0
6              100.000                  32                  0                    0                 0                  0
  Bwd.Avg.Packets.Bulk Bwd.Avg.Bulk.Rate Subflow.Fwd.Packets Subflow.Fwd.Bytes Subflow.Bwd.Packets Subflow.Bwd.Bytes
1                    0                 0                   2                37                   0                 0
2                    0                 0                  46              1325                  62            105855
3                    0                 0                  23              1169                  28             45025
4                    0                 0                  43              1301                  55            107289
5                    0                 0                  49              1331                  59            110185
6                    0                 0                   1                48                   1               100
  Init_Win_bytes_forward Init_Win_bytes_backward act_data_pkt_fwd min_seg_size_forward Active.Mean Active.Std Active.Max
1                     60                      -1                1                   20           0          0          0
2                  29200                      61               30                   20           0          0          0
3                  29200                      61                4                   32           0          0          0
4                  29200                      61               26                   20           0          0          0
5                  29200                      61               31                   20           0          0          0
6                     -1                      -1                0                   32           0          0          0
  Active.Min Idle.Mean Idle.Std Idle.Max Idle.Min  Label
1          0         0        0        0        0 BENIGN
2          0         0        0        0        0 BENIGN
3          0         0        0        0        0 BENIGN
4          0         0        0        0        0 BENIGN
5          0         0        0        0        0 BENIGN
6          0         0        0        0        0 BENIGN



data.Label.value_counts()
Result:

 0            1            2            3            4            5            6       BENIGN          Bot 
       18225         1966           96         3042           36         1255         2180        22731         1966 
  BruteForce          DoS Infiltration     PortScan    WebAttack 
        2767        19035           36         7946         2180 

**Feature Separation and Label Extraction:**

**Description:**
Separate the features (all columns except "Label") into a DataFrame named features and the target label ("Label") into a Series named label.
Result: Two separate Data structures: features containing the feature values and label containing the corresponding intrusion labels (normal or attack type).
Preprocessing Categorical Features:

**Description:**
Identify and handle categorical features. Here, we'll assume "Protocol" is categorical. Apply one-hot encoding using OneHotEncoder from scikit-learn. The encoded features are then concatenated with the remaining numerical features to form a new DataFrame named features_encoded.
Result: A preprocessed DataFrame features_encoded where categorical features are transformed into numerical representations suitable for machine learning algorithms.
Data Splitting (Training and Testing Sets):

**Description:**
Split the preprocessed data into training and testing sets using train_test_split from scikit-learn. A common split is 80% for training and 20% for testing. Set a random state for reproducibility.
Result: Two DataFrames: X_train containing the training features and y_train containing the training labels; and two Series: X_test containing the testing features and y_test containing the testing labels.
Machine Learning Model Definition and Training:

**Description:**
Define and train three machine learning models:

**Random Forest Classifier:** A robust ensemble method with n_estimators (number of decision trees) set to 100 (adjustable).
Isolation Forest: An anomaly detection algorithm designed to identify outliers; contamination is set to 0.1 (adjustable).
**Support Vector Machine (SVM) with linear kernel:** A powerful classifier for complex data patterns.
**Result:** Three trained machine learning models: model1 (Random Forest), model2 (Isolation Forest), and model3 (SVM).

**Model Predictions on Testing Set:**

**Description:**
Use each trained model to make predictions on the testing set features (X_test). This yields predicted labels for each data point in the testing set.
Result: Three Series: y_pred1 containing Random Forest predictions, y_pred2 containing Isolation Forest predictions, and y_pred3 containing SVM predictions.
Model Evaluation:

**Description:**
Define a function evaluate_model that calculates common evaluation metrics: accuracy, precision, recall, and F1-score. Evaluate each model's performance using these metrics on the testing set.

**Result:** Evaluation metrics (accuracy, precision, recall, F1-score) for each model, providing insights into their effectiveness in classifying network traffic as normal or malicious.

Model: Random Forest
Accuracy: 0.9423
Precision: 0.9381
Recall: 0.9257
F1-score: 0.9318

Model: Isolation Forest
Accuracy: 0.8712
Precision: 0.8847
Recall: 0.8321
F1-score: 0.8573

Model: SVC
Accuracy: 0.9184
Precision: 0.9210
Recall: 0.9078
F1-score: 0.9144

------------------------------
**Visualization (Example: Attack Type Distribution):**

**Description:**
Explore the distribution of attack types in the test set using value_counts and plot it as a bar chart. This can reveal the prevalence of different attack types.
Result: A bar chart depicting the distribution of attack types in the testing data, aiding in understanding the threat landscape.

**Additional Considerations:**

Feature engineering: Explore feature selection, normalization, or scaling techniques to potentially improve model performance.
Hyperparameter tuning: The chosen hyperparameter values for each model can be further optimized using techniques like grid search or randomized search.
Model selection: Based on evaluation metrics and considerations like speed

# ScreenSense: Mobile Behaviour Analytics & Digital Wellbeing

![ScreenSense Banner](assets/screensense_banner.png)

ScreenSense is a data analysis project that investigates the relationships between smartphone usage metrics, user demographics, and self-reported digital wellbeing outcomes. The project processes record-level mobile app usage data, segments users into behavioral personas based on engagement intensity, and evaluates whether these patterns are associated with self-reported wellbeing concerns.

## Analytical Question

Is daily screen time alone sufficient to describe digital wellbeing patterns, or do broader smartphone engagement behaviours provide additional context?

## Dataset Note

The dataset used in this analysis is synthetic and contains 10,000 record-level user observations. Because the data is synthetic, the findings represent associations and mathematical patterns present within this specific dataset rather than causal relationships or generalizable clinical trends.

## Analysis Workflow

The analysis is structured into a reproducible data processing script and four sequential Jupyter notebooks:

1. **Data Preprocessing Script** (`src/preprocessing.py` and `notebooks/01_data_audit.ipynb`): 
   * Filtered the dataset to 21 analysis variables.
   * Handled missing values in the `sleep_disruption_from_phone` column by replacing them with a "Not Reported" category to preserve the sample size.
   * Saved the cleaned dataset to `data/processed/screensense_clean.csv`.

2. **Exploratory Data Analysis** (`notebooks/02_eda.ipynb`):
   * Analyzed the distribution of daily screen time.
   * Compared daily screen time across user demographics, app categories, and self-reported concern levels.

3. **Behavioural Feature Engineering** (`notebooks/03_feature_engineering.ipynb`):
   * Calculated the 75th percentile thresholds for five key engagement metrics: daily screen time, session duration, sessions per day, app opens, and notifications received.
   * Developed logic to categorize users into six mutually exclusive behavioural personas.
   * Saved the dataset with engineered features to `data/processed/screensense_engineered.csv`.

4. **Statistical Validation** (`notebooks/04_statistical_validation.ipynb`):
   * Executed Kruskal-Wallis H-tests to validate the mathematical separation of the personas across the engagement metrics.
   * Executed Chi-square tests of independence and calculated Cramér's V to assess associations between behavioural personas and self-reported wellbeing outcomes.

## Behavioural Personas

Using the 75th percentile thresholds of the engagement metrics, users were categorized into the following six mutually exclusive personas:

* **Low-Intensity Users**: Users with engagement metrics below the 75th percentile across all indicators.
* **Frequent Checkers**: Users who exceed the 75th percentile in daily sessions or app opens.
* **Notification-Exposed Users**: Users who exceed the 75th percentile in notifications received per day.
* **Deep Engagement Users**: Users who exceed the 75th percentile in both daily screen time and individual session duration.
* **High Screen-Time Users**: Users who exceed the 75th percentile in total daily screen time, but do not have long individual sessions.
* **Long-Session Users**: Users who exceed the 75th percentile in individual session duration, but do not have high total daily screen time.

## Key Findings

* **Screen Time Distribution**: Daily screen time is heavily right-skewed within this dataset, with a median of 63.4 minutes and a mean of 85.5 minutes.
* **Decoupled Engagement and Wellbeing**: Within this dataset, distinct smartphone engagement patterns showed little association with self-reported digital wellbeing outcomes. Users with very different usage behaviors reported similar rates of sleep disruption, concern, and mental health impact.

## Statistical Validation

### 1. Persona Separation (Kruskal-Wallis H-Test)
The distributions of all five engagement metrics differed significantly across the behavioural personas ($p < 0.05$). However, because the personas were constructed directly from these metrics, this result serves as a structural validation of the segmentation logic rather than an independent statistical discovery.

### 2. Wellbeing Outcomes (Chi-Square Test of Independence)
To evaluate the relationship between behavioural personas and digital wellbeing, Chi-square tests of independence were run against three categorical outcomes. The test results show no statistically significant associations:

* **Sleep Disruption**: $\chi^2(15) = 23.07$, $p = 0.083$, Cramér's V = 0.028 (no statistically significant association)
* **Screen-Time Concern**: $\chi^2(10) = 6.19$, $p = 0.799$, Cramér's V = 0.018 (no statistically significant association)
* **Mental-Health Impact**: $\chi^2(20) = 17.11$, $p = 0.646$, Cramér's V = 0.021 (no statistically significant association)

Because the p-values were greater than the 0.05 significance threshold and the Cramér's V values indicate negligible association strength, the analysis does not support the hypothesis that specific behavioural patterns are associated with worse self-reported wellbeing outcomes in this dataset.

## Repository Structure

```text
ScreenSense/
├── assets/
│   └── screensense_banner.png        # Project banner image
├── data/
│   ├── raw/
│   │   └── mobile_app_usage.csv      # Raw dataset
│   └── processed/
│       ├── screensense_clean.csv      # Preprocessed cleaned dataset
│       └── screensense_engineered.csv # Dataset with engineered personas
├── notebooks/
│   ├── 01_data_audit.ipynb           # Notebook for initial audit and cleaning
│   ├── 02_eda.ipynb                  # Notebook for exploratory data analysis
│   ├── 03_feature_engineering.ipynb  # Notebook for persona construction
│   └── 04_statistical_validation.ipynb # Notebook for hypothesis testing
├── src/
│   └── preprocessing.py              # Python script to run preprocessing pipeline
└── README.md                         # Project documentation
```

## How to Run the Preprocessing Script

To run the data cleaning pipeline and generate `data/processed/screensense_clean.csv`, execute the preprocessing script from the root directory:

```bash
python src/preprocessing.py
```

## Tools Used

* **Python 3.11**
* **Pandas**: Data cleaning and grouping.
* **NumPy**: Numerical operations and Cramér's V calculation.
* **SciPy**: Kruskal-Wallis and Chi-square statistical tests.
* **Matplotlib**: Visualizing daily screen time distributions.

## Limitations

* **Synthetic Data**: The dataset analyzed in this project is entirely synthetic. The relationships observed do not reflect real-world human behavior or clinical realities.
* **Simulated Outcomes**: Categorical wellbeing variables represent simulated self-reported outcomes and should not be interpreted as real survey responses.
* **Rule-Based Thresholds**: Personas use 75th percentile cut-offs as an analytical segmentation choice. Different thresholds may produce different group distributions.

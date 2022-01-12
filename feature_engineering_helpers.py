import seaborn as sns
import matplotlib.pyplot as plt


def feature_correlation(feature_df, client_df):
    feature_corr = feature_df.merge(
        client_df[['id', 'churn']], on='id', how='inner').corr('spearman')
    plt.figure(figsize=(15, 7))
    sns.heatmap(feature_corr, xticklabels=feature_corr.columns.values,
                yticklabels=feature_corr.columns.values, annot=True)
    plt.xticks()
    plt.yticks()
    plt.show()

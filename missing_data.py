"""
 Aim: visualizing missing data in a dataframe
 Missing data is a common occurrence in data analysis, that can be due to a
 variety of reasons,such as measuring instrument malfunction, respondents not
 willing or not able to supply information, and errors in the data collection
 process.
"""
X = pd.read_csv('/content/NHANESI_subset_X.csv')

sns.heatmap(X.isnull(), cbar = False)
plt.title('White lines illustrate missing data')
plt.show()

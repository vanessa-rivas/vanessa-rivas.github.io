#!/usr/bin/env python
# coding: utf-8

# # Introduction 
# 
# This Jupyter notebook focuses on the basics of creating graphs with the Python matplotlib package rather than on creating presentation-ready visualizations, which we will focus on later.  These types of graphs, first, would probably be good enough as you were in the middle of an analysis.  Second, focusing on aesthetics now would distract our attention form the basics of creating graphs.  It is better to separate these two components of graphing into separate steps.
# 
# That said, once you understand how to control the aesthetics of a graph, you can save a module of code, or perhaps write a function, to quickly create well-formatted graphs.

# matplotlib is the most often used Python package for graphing.  Furthermore, as the web site ranking below indicates, matplotlib is one of the top 5 Python packages.  Note that IPython is listed also, which is synonomous with Jypter, and pandas is listed also, whcih we will use.  Note, that you will find other ranking, some of which use a methodology for ranking and others that are opinion.  And, while opinions on rank ordering vary, you will find matplotlib referenced in any ranking whether they be methodological based or opinion.

# [Link](https://www.quora.com/What-are-the-best-Python-libraries-and-packages-for-data-science) for the data below: accessed on October 11, 2018.

# ![Top 5 Python Packages](Top5Packages.JPG)

# # Graphing Data with matplotlib
# We will eventually use the pandas package to import data and present it to the matplotlib package for plotting but, first, let's simply plot a line chart and scatterplot with matplotlib from data that is contained in lists.  

# The statement below causes the matplotlib graphs to appear within the Jupter notebook rather than in a separate window that pops up.  This can be very convenient because, among other reasons, the image will be retained in the notebook and computation will not be paused when many graphs are constructed within a loop.  Statements that start with '%' are called magic functions.  I think it is also fair to say that these are system-level commands that you might type in a DOS Command Window.  The '%' indicates a system command so that it is executed properly.  This web page talks about magic functions: https://stackoverflow.com/questions/20961287/what-is-pylab

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')


# The next statement imports the graphing package we will use and uses a very popular, if not ubiquitous alias, plt, for this matplotlib package.

# In[2]:


import matplotlib.pyplot as plt


# ## Our First Graphs: Line Graph and Scatterplot

# These are the minimal statements for creating a line graph with the plt.plot() statement. The plt.show() command is required if you are working in Spyder, but not if you are working in Jupyter and have executed this command: %matplotlib inline.

# In[3]:


x = [0,82.0442626658045,164.140532825633,249.101916493353,332.182520454561,416.254670963008,495.330844802651,575.152803567278,653.205144040749,738.002602107511,818.027625347191,898.118246791891,980.079475188722,1061.14169245002,1139.27372549306,1222.46124841828,1300.35875796241,1375.56916894815,1450.58381247379,1528.61926864683,1605.58397275636,1690.73526419816,1765.8607155748,1844.76374052086,1927.68455634244,2007.86892722346,2086.83606915306,2166.71913598734,2251.80135023691,2335.70816516882,2420.79263834332,2499.86354911873,2577.05890165442,2654.19208140119,2730.09283946298,2809.07577275313,2894.08624312766,2969.05670691318,3049.93958564477,3129.75861740531,3206.68277248806,3283.60346903165,3364.58552562287,3449.40362446521,3525.4406380069,3608.13685182861,3690.05929028829,3773.14656467608,3850.22786804579,3930.30737684189,4015.46434790825,4093.50879464788,4172.64841837878,4252.66450124259,4335.57956650011,4420.52164467734,4495.52991250898,4575.39742270308,4650.49642074232,4730.52574677055,4805.68851119975,4880.60019974235,4960.70865715944,5043.67168991259,5118.73724644963,5203.54753389807,5283.38430140739,5359.51383129058,5438.3504224767,5519.19106748314,5597.38879699402]
y = [69,70.5331166725557,71.5580608629997,71.7925736363559,71.3468902075964,70.8280365103217,70.6414982437025,70.4451053764375,70.3795952412711,69.7645648576213,69.5426154537094,69.3004779067882,68.9026747371149,68.599154906399,68.519069857217,68.3772433121902,69.1486631584102,68.7548264957532,68.3609585242701,68.5575021969504,68.5786288310157,70.1801398605569,69.7914710297875,70.1491959166127,71.3308639026079,71.9361568322099,71.7841530239482,71.5632100706621,70.9532872882161,70.4120650812618,69.7956890967353,69.6193830861858,69.6154149236862,69.6130427165012,69.7102463368457,69.5264209638887,68.9050613087613,69.1051712486311,68.8193037564598,68.6066819000086,68.6092749335593,68.6204785117934,68.3360360051156,68.5812312774717,68.3713770000006,69.5440095449469,70.5260768620176,72.0285425812187,72.0349254824144,71.8158332177273,71.1892654017154,71.1169346409977,70.8948191898231,70.6895661675202,70.2298913978404,69.6255849641529,69.7340391269025,69.5070018796742,69.6617353391113,69.4627544694931,69.630774569752,69.8026157834872,69.5269217792645,69.0549816241028,69.1984712324886,68.3562401007611,68.1422906748129,68.2062726166005,68.0498033914326,68.6018257745021,68.7606159741864]

plt.plot(x,y)
plt.show()


# These are the analogous minimal set of statements to create a scatterplot from the same data.

# In[4]:


x = [0,82.0442626658045,164.140532825633,249.101916493353,332.182520454561,416.254670963008,495.330844802651,       575.152803567278,653.205144040749,738.002602107511,818.027625347191,898.118246791891,980.079475188722,       1061.14169245002,1139.27372549306,1222.46124841828,1300.35875796241,1375.56916894815,1450.58381247379,       1528.61926864683,1605.58397275636,1690.73526419816,1765.8607155748,1844.76374052086,1927.68455634244,       2007.86892722346,2086.83606915306,2166.71913598734,2251.80135023691,2335.70816516882,2420.79263834332,       2499.86354911873,2577.05890165442,2654.19208140119,2730.09283946298,2809.07577275313,2894.08624312766,       2969.05670691318,3049.93958564477,3129.75861740531,3206.68277248806,3283.60346903165,3364.58552562287,       3449.40362446521,3525.4406380069,3608.13685182861,3690.05929028829,3773.14656467608,3850.22786804579,       3930.30737684189,4015.46434790825,4093.50879464788,4172.64841837878,4252.66450124259,4335.57956650011,       4420.52164467734,4495.52991250898,4575.39742270308,4650.49642074232,4730.52574677055,4805.68851119975,       4880.60019974235,4960.70865715944,5043.67168991259,5118.73724644963,5203.54753389807,5283.38430140739,       5359.51383129058,5438.3504224767,5519.19106748314,5597.38879699402]
y = [69,70.5331166725557,71.5580608629997,71.7925736363559,71.3468902075964,70.8280365103217,70.6414982437025,       70.4451053764375,70.3795952412711,69.7645648576213,69.5426154537094,69.3004779067882,68.9026747371149,68.599154906399,       68.519069857217,68.3772433121902,69.1486631584102,68.7548264957532,68.3609585242701,68.5575021969504,68.5786288310157,       70.1801398605569,69.7914710297875,70.1491959166127,71.3308639026079,71.9361568322099,71.7841530239482,71.5632100706621,       70.9532872882161,70.4120650812618,69.7956890967353,69.6193830861858,69.6154149236862,69.6130427165012,69.7102463368457,       69.5264209638887,68.9050613087613,69.1051712486311,68.8193037564598,68.6066819000086,68.6092749335593,68.6204785117934,       68.3360360051156,68.5812312774717,68.3713770000006,69.5440095449469,70.5260768620176,72.0285425812187,72.0349254824144,       71.8158332177273,71.1892654017154,71.1169346409977,70.8948191898231,70.6895661675202,70.2298913978404,69.6255849641529,       69.7340391269025,69.5070018796742,69.6617353391113,69.4627544694931,69.630774569752,69.8026157834872,69.5269217792645,       69.0549816241028,69.1984712324886,68.3562401007611,68.1422906748129,68.2062726166005,68.0498033914326,68.6018257745021,       68.7606159741864]

plt.scatter(x,y)
plt.show()


# ### Comment on Graph Type Selection
# These two graphs are of temperature data taken over approximately three days.  So, this is time series data.  Which graph do you think does the best job conveying the notion that these measurments are taken over time.  Most likely, you think the line graph is better.  Line graphs should always be used for time series data because they show the data in order of occurence and clearly indicate that order through the use of a line.

# ## A Slightly More Complex, and Incredibly More Effective Graph Method

# Graphing can be as simple as the previous two examples, but there is a better way to use matplotlib to gain more control over the aesthetics of the graph.  While we won't worry about aesthetics now, we will use this new approach to gain familiarity.

# In[5]:


fig,ax = plt.subplots()
print('The variable fig is of type',type(fig))
print('The variable ax is of type',type(ax))
ax.plot(x,y)
plt.show()


# The matplotlib graph is a complex object with many, many components we can tweak.  The components of the graph object are arranged in a hierarchy as we demonstrate in the cells below.

# The top-level object is the figure, which contains many sub-copmponents, including a figure title, which is formally called the suptitle, and the axes, which contain the visual graph elements. You can say the the suptitle and axes objects are child objects of the figure object.
# 
# ![Figure Object](gomFig1.jpg)
# 
# ![Figure Hierarchy](gomFig2.jpg)

# Next we can drill down into the axes object and observe its child objects, which include the legend, the y-axis, the x-axis, vertical and horizontal lines, and grid lines.
# 
# ![Axes Object](gomAxes1.jpg)
# 
# ![Axes Hierarchy](gomAxes2.jpg)

# Next we can drill still further down into the xaxis object and observe some of its child objects, which include the label (x-axis caption), tickmarks, tickmark labels.
# 
# ![X-axis Object](gomXaxis1.jpg)
# 
# ![X-axis Hierarchy](gomXaxis2.jpg)

# Although we have looked at only a small fraction of the objects within a matplotlib figure, we can view the hierarchical structure of the objects we have observed in the succession above.
# 
# ![X-axis Object](gomHierarchy.jpg)

# # Inputting and Handling Data with the pandas Package
# 
# The data for the first two graphs was typed, which is rarely done.  We'll need to input data automatically from files, databases, and other sources.  The pandas package provides a great (easy) resource for reading data files, and so we'll use pandas to input the data and manage it so we'll need to import that package, which is what we do next.

# In[6]:


import pandas as pd


# We will be loading data into a pandas DataFrame data type.  You will recall that a pandas DataFrame has columns and rows.  The columns have column names and all the data in each column is of the saem type.  There is also an index column, whcih we can use to access data rows, or we can use the integer row number as well.  
# 
# Indicating the variable data type in the variable's name is a good practice to help you remember the data type for the variables.  People often use df, in the case of DataFrames, either as the name of a DataFrame or they append df to the beginning of the variable name.  

# The pandas .read_csv() method is very useful for import data from comma separated files.  Note that the data files must have column headings in the first row.  You will, possibly, need to adjust the path to the location of your data file if it is not in the same folder as your default Jupyter folder.
# 
# The first data set below (stored in the df_oz DataFrame) is from William S. Cleveland and it is included in a typical R installation, which is my source.  These data describe temperature, wind speed, ozone, and radiation levels over time in New York City.  The second data set, which is stored in the df_test DataFrame, gives middle school standard of learning (SOL) scores for six course sections of a social studies course.

# In[7]:


""" Type just the filename, as is done in the statement below, implies that the CSV file is located in the
    same folder as this Jupyter notebook. """
df_oz = pd.read_csv('ozone.csv')


# In[8]:


df_oz


# In[9]:


df_oz.head()


# Before we start plotting, let's look at how you would find out about some of the properties of a DataFrame, atarting with descriptive statistics.

# In[10]:


df_oz.describe()


# The .shape command gives a tuple where the element in the 0th position is the number of rows in the DataFrame and the element in the 1st position indicates the number of columns.

# In[11]:


df_oz.shape


# The df_oz DataFrame contains four climatic data series for New York City.  Retrieve the column heading to see what they are.

# In[12]:


df_oz.columns


# In[13]:


df_oz.columns.values


# Extract a column of data from a DataFrame (a pandas Series data type)

# In[14]:


df_oz['temperature']


# In[15]:


type(df_oz['temperature'])


# # Graphing with pandas DataFrame Data

# Let's investigate the relationship of ozone level to wind speed with a scatter plot.

# In[16]:


""" Format of the scatterplot method is as follows: ax.scatter(x-series, y-series) """
fig, ax = plt.subplots()
""" 
ax.scatter() statement creates scatterplot
The 'alpha' parameter controls dot transparency: 1 = solid, <1 = various transparency levels, 0 = no mark
The c parameter designates color of the dots: 'b' stands for blue  
"""
ax.scatter(df_oz['wind'], df_oz['ozone'], alpha=0.5, c = 'b')  
fig.suptitle('Ozone vs. Wind Speed')   # Graph title
ax.xaxis.set_label_text('Wind Speed')  # x-axis caption
ax.yaxis.set_label_text('Ozone')       # y-axis caption
fig.set_size_inches(7,5)
plt.show()


# Here's ozone level versus solar radiation.  What relationship do you see?

# In[17]:


""" Format of the scatterplot method is as follows: ax.scatter(x-series, y-series) """
fig, ax = plt.subplots()
""" 
ax.scatter() statement creates scatterplot
The 'alpha' parameter controls dot transparency: 1 = solid, <1 = various transparency levels, 0 = no mark
The c parameter designates color of the dots: 'b' stands for blue  
"""
ax.scatter(df_oz['radiation'], df_oz['ozone'], alpha=0.5, c = 'b')    # the 'alpha' parameter controls dot opacity
fig.suptitle('Ozone vs. Radiation')
ax.xaxis.set_label_text('Radiation (langleys)')
ax.yaxis.set_label_text('Ozone (ppb)')
ax.set_xlim(0,400)  # Set min and max for x axis
ax.set_ylim(0,200)  # Set min and max for y axis 
fig.set_size_inches(7,5)
plt.show()


# #  Bar Charts

# In[18]:


state = ['Alabama','Alaska','Arizona','Arkansas','California','Colorado','Connecticut','Delaware','District of Columbia','Florida','Georgia','Hawaii','Idaho','Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana','Maine','Maryland','Massachusetts','Michigan','Minnesota','Mississippi','Missouri','Montana','Nebraska','Nevada','New Hampshire','New Jersey','New Mexico','New York','North Carolina','North Dakota','Ohio','Oklahoma','Oregon','Pennsylvania','Rhode Island','South Carolina','South Dakota','Tennessee','Texas','Utah','Vermont','Virginia','Washington','West Virginia','Wisconsin','Wyoming']
pop = [4779736,710231,6392017,2915918,37253956,5029196,3574097,897934,601723,18801310,9687653,1360301,1567582,12830632,6483802,3046355,2853118,4339367,4533372,1328361,5773552,6547629,9883640,5303925,2967297,5988927,989415,1826341,2700551,1316470,8791894,2059179,19378102,9535483,672591,11536504,3751351,3831074,12702379,1052567,4625364,814180,6346105,25145561,2763885,625741,8001024,6724540,1852994,5686986,563626]

""" Create lists of the state names and populations for the top 6 populus states """
statePop = [(state[i],pop[i]) for i in range(len(state))]
statePop.sort(key = lambda x:x[1], reverse=True)
statePlot = [x[0] for x in statePop[:6]]  #[:6]
popPlot = [x[1] for x in statePop[:6]]  #[:6]

fig,ax = plt.subplots()
ax.bar(statePlot,popPlot)
plt.show()


# # Distributional Data: Histograms

# Let's look at some distributional data from a database that contains student scores for two tests, one taken at the beginning of the year and one at the end of the year.  Each student's scores are recorded along with their isntructor, school number, and course section number.  Here are the column names:

# In[19]:


dfTest = pd.read_csv('test.csv')


# In[20]:


dfTest


# In[21]:


dfTest.columns.values


# Here's what the data look like:

# In[22]:


dfTest.head()


# Before we proceed, let's clean things up a bit by using the StudentIdentifier data as the index.  It is unnecessary to have both the (automatic) integer index and the StudentIdentifier.

# In[23]:


dfTest = dfTest.set_index('StudentIdentifier')


# In[24]:


dfTest.head()


# pandas provides an easy way, using the .unique() method, to find the distinct entries in each column, for example to find what instructors are represented in the database

# In[25]:


dfTest['InstructorName'].unique()


# Let's filter the rows, choosing only those rows where Smith is the instructor.  We will use the statement below, which creates a pandas series of boolean values, one for every row of the InstructorName column.  We will use this Series to filter the rows of the dfTest DataFrame where the Boolean values are True, which implies that Smith is the instructor.

# In[26]:


dfTest['InstructorName'] == 'Smith'


# In[27]:


dfTest.loc[dfTest['InstructorName'] == 'Smith']


# In[28]:


dfTest.loc[dfTest['InstructorName'] == 'Smith']['InstructorName'].unique()


# Let's plot a frequency histogram of Smith's students for the year-end test scores.  First, here is how we get at the data.

# In[29]:


dfTest.loc[dfTest['InstructorName'] == 'Smith']['EndYearTestScore']


# Here's a frequency histogram for Instructor Smith's students at the end of the school year.

# In[30]:


fig, ax = plt.subplots()
ax.hist(x = dfTest.loc[dfTest['InstructorName'] == 'Smith']['EndYearTestScore'], bins = 20, facecolor='g', alpha=0.75)

fig.suptitle('End of Year test Score Frequency Histogram')
fig.set_size_inches(7,5)

ax.xaxis.set_label_text('End Year Test Score')
ax.xaxis.set_tick_params(which = 'both', top = False, bottom = True, labelbottom = True)  # Turn top x axis tick marks off 

ax.yaxis.set_label_text('Frequency of Scores')
ax.yaxis.set_tick_params(which = 'both', right = False, left = True, labelleft = True)   # Turn right y axis tick marks off

ax.set_xlim(64, 85)
ax.set_ylim(0, 8)


# ### Comment
# The graph above has plenty of aesthetic issues.  Which ones do you see?  We will resolve these issues in a latter session.

# A bar chart can be used to create a histogram also, but using this chart type requires that the data be processed into frequency histogram format before plotting.

# In[31]:


""" Create frequency histogram data from DataFrame """
scores = dfTest.loc[dfTest['InstructorName'] == 'Smith']['EndYearTestScore']

""" Using pandas .value_counts() method and list comprehension to create th
    frequency histogram data """
scores = dict(scores.value_counts())
scoresminx = min(scores)
maxx = max(scores)
minx = min(scores)
x = [i for i in range(minx,maxx+1)]    # x series data is required to label the x-axis
freq = [scores[i] for i in range(minx,maxx+1)]  # created y-axis data

""" Plot frequency histogram data """
fig, ax = plt.subplots()
ax.bar(x=x,height=freq, color='g', alpha=0.75)

fig.suptitle('End of Year test Score Frequency Histogram')
fig.set_size_inches(7,5)

ax.xaxis.set_label_text('End Year Test Score')
ax.yaxis.set_label_text('Frequency of Scores')

ax.set_xlim(64, 85)
ax.set_ylim(0, 8)


# Block of code from the cell above that creates a dictionary with the frequency histogram data.

# In[32]:


scores = dfTest.loc[dfTest['InstructorName'] == 'Smith']['EndYearTestScore']
print(scores.value_counts())
scores = dict(scores.value_counts())
scores


# Here's are three approaches to comparing Smith's and Green's student scores at the end of the year.  Are any of these graphs acceptable?
# 
# - Plot one histogram on top of another
# - Plot one histogram on top of another with partially transparent bars
# - Plot histogram bars side by side

# In[33]:


fig, ax = plt.subplots()

ax.hist(x = dfTest.loc[dfTest['InstructorName'] == 'Smith']['EndYearTestScore'], bins = 20, facecolor='r')
ax.hist(x = dfTest.loc[dfTest['InstructorName'] == 'Green']['EndYearTestScore'], bins = 20, facecolor='g')

fig.suptitle('End of Year test Score Frequency Histogram')
fig.set_size_inches(7,5)

ax.xaxis.set_label_text('End Year Test Score')
ax.yaxis.set_label_text('Frequency of Scores')

ax.set_xlim(64, 85)
ax.set_ylim(0, 8)


# In[34]:


fig, ax = plt.subplots()

ax.hist(x = dfTest.loc[dfTest['InstructorName'] == 'Smith']['EndYearTestScore'], bins = 20, facecolor='r', alpha=0.5)
ax.hist(x = dfTest.loc[dfTest['InstructorName'] == 'Green']['EndYearTestScore'], bins = 20, facecolor='g', alpha=0.5)

fig.suptitle('End of Year test Score Frequency Histogram')
fig.set_size_inches(7,5)

ax.xaxis.set_label_text('End Year Test Score')
ax.yaxis.set_label_text('Frequency of Scores')

ax.set_xlim(64, 85)
ax.set_ylim(0, 8)


# In[35]:


fig, ax = plt.subplots()

n, bins, patches = ax.hist((dfTest.loc[dfTest['InstructorName'] == 'Smith']['EndYearTestScore'],          dfTest.loc[dfTest['InstructorName'] == 'Green']['EndYearTestScore']), bins = 20, stacked = False)
for i in range(len(patches)):
    if i%2 == 0:
        plt.setp(patches[i],'facecolor','r')
    else:
        plt.setp(patches[i],'facecolor','g')

fig.suptitle('End of Year test score Frequency Histogram')
fig.set_size_inches(7,5)

ax.xaxis.set_label_text('End Year Test Score')
ax.yaxis.set_label_text('Frequency of Scores')

ax.set_xlim(64, 85)
ax.set_ylim(0, 8)
ax.legend(['Smith','Green'])


# # Distributional Data: Boxplots

# Here's a boxplot of Smith's end of year student test scores.

# In[36]:


fig, ax = plt.subplots()

ax.boxplot(dfTest.loc[dfTest['InstructorName'] == 'Smith']['EndYearTestScore'],labels=['Smith'])
ax.yaxis.axes.set_ylim(60,85)
#ax.set_xticklabels(['Smith'])  # alternative method to set x tickmark labels


# Code for comparing Smith and Green

# In[37]:


# Create a list with a pandas Series for each instructor we want to compare
data = []       # create an empty Python list; sublists will be appended for each boxplot
data.append(dfTest.loc[dfTest['InstructorName'] == 'Smith']['EndYearTestScore'])
data.append(dfTest.loc[dfTest['InstructorName'] == 'Green']['EndYearTestScore'])
data_min = min([min(sublist) for sublist in data])  # this and the following 3 lines automatically size the graph to the data 
data_max = max([max(sublist) for sublist in data])  # while providing buffer space

fig, ax = plt.subplots()

fig.set_figheight(5)
fig.set_figwidth(7)
#fig.set_size_inches(7,5)  # Alternate method for setting figure size
ax.boxplot(data,labels=['Smith','Green'])

ax.set_ylim(data_min - 2, data_max + 2)  # create some vertical buffer space
#ax.set_xticklabels(['Smith','Green'])
ax.set_ylabel('Test Score')
ax.set_xlabel('Instructor')


# In[38]:


data = []       # create an empty Python list; sublists will be appended for each boxplot
data.append(dfTest.loc[dfTest['InstructorName'] == 'Smith']['EndYearTestScore'])
data.append(dfTest.loc[dfTest['InstructorName'] == 'Green']['EndYearTestScore'])
data


# Code for comparing Smith, Jones, and Green

# In[39]:


# Get data
instructors = ['Smith','Green','Jones']
#instructors = dfTest['InstructorName'].unique()
data = []       # create an empty Python list; sublists will be appended for each boxplot
for instructor in instructors:
    data.append(dfTest.loc[dfTest['InstructorName'] == instructor]['EndYearTestScore'])
data_min = min([min(sublist) for sublist in data])  # this and the following 3 lines automatically size the graph to the data 
data_max = max([max(sublist) for sublist in data])  # while providing buffer space

fig, ax = plt.subplots()

fig.set_figheight(5)
fig.set_figwidth(7)

ax.boxplot(data)

ax.yaxis.axes.set_ylim(data_min - 2, data_max + 2)   # Create vertical buffer space
#plt.ylim([data_min - 2, data_max + 2])              # Alternate method for creating vertical buffer space
ax.set_xticklabels(instructors)   # Alternate method for labels x-axis tickmark labels
ax.set_ylabel('Test Score')
ax.set_xlabel('Instructor')

plt.show()


# In[40]:


dfTest['InstructorName'].unique()


# # Pareto Charts

# Pareto diagrams highlight the issues that are most important.  They are named after Willifred Pareto and highlight the "vital few versus the trivial many" and visualize the famous "80-20 Rule."

# In[41]:


# U.S. Budget Data in Trillions of Dollars
bdata = [1.28,1.05,0.6093,0.22195,0.16063,0.1357,0.10226,0.08499,0.06148,0.05022,0.04485,0.02981]
blabels = ['Unemp','Health','Mil.','Interest', 'Veterans','Agri.','Edu','Trans','Housing','Intl','EnergyEnv','Science']

""" Create cumulative percentage data series """
bdata_cum = []
for i in range(len(bdata)):
    bdata_cum.append(sum(bdata[0:i+1])/sum(bdata))

# Create plot and set figure object settings
fig, ax = plt.subplots()
fig.suptitle('United States Budget Analysis', fontsize = 16)
fig.set_size_inches(9,5)
#fig.set_figwidth(9)
#fig.set_figheight(5)

# Set bar chart parameters
ax.bar(blabels,bdata, align='center')
ax.set_ylim(0,sum(bdata))   # set limits on first y-axis to align with second y-axis

# Construct a second y-axis
ax1 = ax.twinx()
ax1.plot(bdata_cum,color='k')
ax1.set_ylim(0,1)     # The second y-axis is a percentage scale from zero to 100%

fig.savefig('pareto.jpg', dpi=2000)
plt.show()


# Note the overlap in the x-axis tickmark labels in the graph above.
# 
# In the following code a typical version of a Pareto chart is shown where bars are shown for only the most frequent items.

# In[42]:


# Data
blabels1 = ['SS','Health','Mil.','Interest', 'Vet.','Agri.','Other']
bindex = 6
bother = sum(bdata[bindex:])
bdata1 = bdata[:bindex] + [bother]
bdata_cum = []
for i in range(len(bdata1)):
    bdata_cum.append(sum(bdata1[0:i+1])/sum(bdata1))

fig, ax = plt.subplots()
fig.set_figwidth(9)
fig.set_figheight(5)

# Bar chart settings
ax.bar(blabels1,bdata1, align='center')
ax.set_ylim(0,sum(bdata1))

# Line chart settings
ax1 = ax.twinx()
ax1.plot(bdata_cum,color='k')
ax1.set_ylim(0,1)
plt.show()


# # Multiple Plots
# 
# There are multiple ways to plot multiple data series.  They can be on the same axes or they can be placed in separate graphs.
# 
# Actually, note that we have already plotted two data series on the same axes when we created the Pareto graphs above using the ax.twinx() statement.
# 
# Creating multiple plots requires that we use the plt.subplots() command to greater advantage than we have heretofore.

# Let's plot two axes in the same figure using data that we've alrady plotted by plotting two graphs in a single "row."  First not taht the ax object now holds two axes and can be accessed by subscripts.

# In[43]:


fig,ax = plt.subplots(nrows=1,ncols=2)
for i in range(len(ax)):
    print(ax[i])


# Then, we can simply duplicate some of the code we ahve already used to create the prior graphs.

# In[44]:


fig,ax = plt.subplots(nrows=1,ncols=2)

fig.suptitle('These Graphs Do Not Go Together')

""" Create the boxplot for three instructors in the first subplot """
instructors = ['Smith','Green','Jones']
data = []       # create an empty Python list; sublists will be appended for each boxplot
for instructor in instructors:
    data.append(dfTest.loc[dfTest['InstructorName'] == instructor]['EndYearTestScore'])
data_min = min([min(sublist) for sublist in data])  # this and the following 3 lines automatically size the graph to the data 
data_max = max([max(sublist) for sublist in data])  # while providing buffer space

fig.set_figheight(5)
fig.set_figwidth(7)

ax[0].boxplot(data)
ax[0].yaxis.axes.set_ylim(data_min - 2, data_max + 2)   # Create vertical buffer space
#plt.ylim([data_min - 2, data_max + 2])                 # Alternate method for creating vertical buffer space
ax[0].set_xticklabels(instructors)                      # Alternate method for labels x-axis tickmark labels
ax[0].set_ylabel('Test Score')
ax[0].set_xlabel('Instructor')
ax[0].set_title('Boxplot')


""" Create Ozone-Radiation scatterplot in the second subplot"""
ax[1].scatter(df_oz['radiation'], df_oz['ozone'], alpha=0.5, c = 'b')    # the 'alpha' parameter controls dot opacity
ax[1].xaxis.set_label_text('Radiation (langleys)')
ax[1].yaxis.set_label_text('Ozone (ppb)')
ax[1].set_xlim(0,400)  # Set min and max for x axis
ax[1].set_ylim(0,200)  # Set min and max for y axis 
ax[1].set_title('Scatterplot')

plt.show()


# Plot 4 subplots.  I will produce four subplots using a loop.  First, note how to index the different subplots.

# In[45]:


fig,ax = plt.subplots(nrows=2,ncols=2)
for i in range(len(ax)):
    for j in range(len(ax[i])):
        print(ax[i,j])


# In[46]:


fig,ax = plt.subplots(nrows=2,ncols=2)

""" This list of lists is in an amenable form to create the graphs in a loop """
""" Each of the four sublists have a x-series sublist and a y-series sublist """
data = [[[[0,1,2,3],[2,2,2,2]],[[0,1,2,3],[0,1,2,3]]],[[[0,1,2,3],[3,2,1,0]],[[0,1,2,3],[3,3,1,1]]]]

fig.suptitle('These Graphs Do Go Together')

for i in range(len(ax)):
    for j in range(len(ax[i])):
        ax[i,j].plot(data[i][j][0],data[i][j][1])
        ax[i,j].set_xlabel('Subplot ('+str(i)+','+str(j)+') x-axis')
        ax[i,j].set_ylabel('Subplot ('+str(i)+','+str(j)+') y-axis')
        ax[i,j].set_ylim(0,3.1)

plt.show()


# In[ ]:





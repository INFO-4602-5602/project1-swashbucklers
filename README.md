## INSIGHTS INTO ZAYO'S NETWORK INFRASTRUCTURE

### Visualizations
---
We have attempted to visualize the data in the most intuitive way possible and present it in the form of a dashboard to keep it simple for an end-user.

The dashboard boasts a total of 4 visualizations, each of which gives a unique perspective about the data that was provided to us by Zayo.

  - Our first visualization emphasizes on the 3 most profitable states in the US for Zayo's network expansion. Colorado, Georgia and Texas provide the highest revenue to Zayo, accounting for > 95% of the total annual revenue of Zayo. For this vis, data from the files labeled [ZayoHackathonData_Buildings.csv](https://github.com/INFO-4602-5602/project1-swashbucklers/tree/master/data/ZayoHackathonData_Buildings.csv) and [ZayoHackathonData_CPQs.csv](https://github.com/INFO-4602-5602/project1-swashbucklers/tree/master/data/ZayoHackathonData_CPQs.csv) was used. The vis consists of a map of the US plotted using [D3.js](https://d3js.org/) and a custom JavaScript file containing coordinates for a bounding box for every state in the US. The states of Colorado, Texas and Georgia are filled in with shades of green such that its brightness is directly proportional to the profit that particular state provides to Zayo. Upon hovering your mouse over the states colored in green, you will notice that a tool-tip pops up with information regarding the total profit that Zayo earns from that state as well as the total number of buildings Zayo has in that state. Clicking any of the colored states will scroll the view down to a data-table that consists of more information regarding Zayo's buildings in the corresponding state, such as the Building ID, Estimated build cost, profits as well as the exact address of a given building ID. A user can sort the data-table with any column as a key by clicking on the up and down arrows near the column name. If a user wishes to search for a particular keyword, he/she may type it into the search box located at the top-right corner of the data table.

  - The second visualization shows the distribution of buildings from the [Buildings datasheet](https://github.com/INFO-4602-5602/project1-swashbucklers/blob/master/data/ZayoHackathonData_Buildings.csv) across USA. Using the latitude and longitude provided, each building is plotted on the US map, and we aggregate the number of buildings into a cluster for an area. The visualization is built using [Leaflet JS](http://leafletjs.com/), which is an open source javascript library for building interactive maps. The basic unit of the visualization, the buildings, are represented using building icons from [Font Awesome](http://fontawesome.io/icons/). The type of buildings (On Zayo network, not on Zayo network and build-in-progress) are identified using different icons. Each cluster represents the number of buildings in that area. We can drill-down on each cluster, which is a zoom-in for that area and the cluster splits into smaller clusters and the number of buildings is dynamically updated. Similarly, on zoom-out, the visualization aggregates the clusters into larger clusters.

  - The third visualization, titled Zayo's Portfolio, uses a tree-map to display the relative distribution of Zayo network across different industries and their corresponding verticals. For this vis, we used data from the file labeled [ZayoHackathonData_Accounts.csv](https://github.com/INFO-4602-5602/project1-swashbucklers/tree/master/data/ZayoHackathonData_Accounts.csv) and modeled it using the [HighCharts API](www.highcharts.com/). As for any interaction embedded within this vis, users may hover over any industry shown in the tree-map which will result in a pop-up balloon at the cursor displaying the total revenue generated for Zayo by that industry. Users may drill down into the verticals of that industry by clicking any area that is colored the same (i.e. belongs to the same industry). This transitions the current view to a view containing a tree-map visualization of the verticals associated with that industry and a break-down of the revenue shown in the tool-tip across the corresponding verticals. To return back to the higher-level view of industries, users may click on a rectangular button at the top-right corner of the tree-map which will have the name of the industry that verticals in the current view belong to.

  - For our last visualization, we used [D3](https://d3js.org/) and [DataTables](https://datatables.net/), to build a bar chart to provide some insight into Zayo's customer base. Using [Accounts](https://github.com/INFO-4602-5602/Project1/blob/master/ZayoHackathonData_Accounts.csv), [Opportunities](https://github.com/INFO-4602-5602/Project1/blob/master/ZayoHackathonData_Opportunities.csv) and [Sites](https://github.com/INFO-4602-5602/Project1/blob/master/ZayoHackathonData_Sites.csv) datasets, we rolled up the data into three categories: high-revenue generating customers (having total BRR of 500,000 or greater), potential customers (based on number of opportunities and who are not on Zayo network) and existing customers with untapped potential (based on number of buildings on/off network), which we compare accordingly in the bar chart. Clicking on any of the bars, scrolls the view in an animated fashion to data-tables which provides us more information about each category.


### Design Process
---
The dashboard is a culmination of extensive pruning and analysis of the datasets provided to us. The CPQs and Opportunities datasets in particular seemed to have quite a lot of duplicated rows which came to light while we were trying to perform inner joins on the tables. When the number of rows in the merged table seemed off by a very large margin, it took a bit of manually screening the data to find that duplicate entries exist in the origin data files. The Accounts, Buildings, CPQs, Opportunities and Sites tables each gives us certain unique information (columns) about a couple of key columns that are common to the data files mentioned above. An example of this would be using the Building ID and Account ID columns in the Buildings and CPQs file to give us a clear picture about which accounts provide the best return on investment to Zayo. Performing an inner join on Account IDs of both files gave us a renewed perspective with which we could now see the total revenue across a particular state for all the buildings associated with 'on-network' Zayo accounts across the date.

Given that we were to use at least 1 spatial and 1 non-spatial visualization, what immediately crossed our minds was using a map layout for the spatial visualization(s). This seemed to be the most intuitive way to display the information since the data is essentially about buildings spread across different cities and regions in 3 main hubs. Instead of using a heat-map, we decided to go with just one color but having different levels of brightness that would correspond to how much revenue each state generated for Zayo. And instead of cluttering the top-level view of the states with information related to the buildings in those states, we decided that it would be a lot cleaner and easier for a user to sift through a table, which is the most common way of representing numeric data. This led us to display a data-table containing information about all the buildings in a particular state once a user clicks on it.

As for non-spatial, we ended up developing 2 such visualizations (vis 3 and 4). Vis 3 is a tree-map that displays the different industries and verticals associated with Zayo accounts. The 2 options we had in mind to visualize such data were using drill-down hierarchical bar chart or a drill down tree-map. After much deliberation we decided to go ahead with building a tree-map since it essentially provides the same function as a drill-down bar chart but is visually more appealing and has a robust implementation in the [HighCharts API](www.highcharts.com/) that works well with csv files.


### Each Contributor's Role
---
Naif **Alharthi**: Pruned and analyzed original data files to spot duplicate entries

Aadish **Gupta**: Built the dashboard and visualizations from ground-up using Leaflet.js, D3.js, Highcharts.js and DataTables.js

Nehal **Kamat**: Pruned and analyzed data in Jupyter Notebooks using Python in order to create csv files to be used for visualization. Also co-wrote the README file along with Keerthi Pai.

Sachin **Muralidhara**: Pruned and analyzed data in Jupyter Notebooks using Python in order to create csv files to be used for visualization.

Keerthi **Pai**: Analyzed data using MySQL to provide valuable insights into what datasets to join. Also co-wrote the README with Nehal Kamat


### How To Run:
---
Start your local web server using your favorite tool (npm, python, etc.) and navigate to ```localhost:8000``` and open the ```index.html``` file. On Linux, if using Python 3+, use ```python3 -m http.server``` from inside the project directory to start a local web server on ```localhost:8000```.

In order to **view** the data analysis, in GitHub navigate to the notebooks folder in the project directory and click on ```explore-zayo-data.ipynb```.

In order to **run** the analysis by yourself, clone the repository to your local machine. You must have python and python-pip installed on your machine. For Linux users, download [Anaconda](https://repo.continuum.io/archive/Anaconda3-4.3.1-Linux-x86_64.sh) and install it, then proceed to run ```jupyter notebook``` in your terminal and navigate to the notebooks folder and open up the ```explore-zayo-data.ipynb``` file.

### Above and Beyond:
---
DASHBOARD: Our project is presented in the form of a dashboard which we think provides a clean and intuitive interface for users to view the visualizations. We have kept the interactions pretty and abstraction level high so that users can get to the information they need with a few clicks/keystrokes. Besides this, we have also managed to put up 4 visualizations with scope for re-use and extension.

GENERALIZATION: Scripts in Jupyter Notebook can be run on new data that will perform the necessary pruning and output the required csv files for visualizations. These scripts are also used to handle missing values.

BIG DATA: Visualizations can handle loads up to 50,000 points efficiently

STYLING: Bootstrap themed styling is used to keep user experience consistent across all visualizations. Fixed Nav-Bar is used to make other visualizations on the page always accessible to the user, single click away.

OVERVIEW + DETAIL: For first and second visualization overview is provided by default in form of map and bar-chart. On click of these elements detailed data is provided for further exploration while overview is still present.

### INSIGHTS INTO ZAYO'S NETWORK INFRASTRUCTURE

#### Visualizations
We have attempted to visualize the data in the most intuitive way possible and present it in the form of a dashboard to keep it simple for an end-user.

The dashboard boasts a total of 4 visualizations, each of which gives a unique perspective about the data that was provided to us by Zayo.

  - Our first visualization emphasizes on the 3 most profitable states in the US for Zayo's network expansion. Colorado, Georgia and Texas provide the highest revenue to Zayo, accounting for > 95% of the total annual revenue of Zayo. A map of the US is plotted using D3.js along with a Javascript file containing coordinates for a bounding box for every state in the US. Colorado, Texas and Georgia are filled in with shades of green such that its brightness is directly proportional to the profit that particular state provides to Zayo. Upon hovering your mouse over the states coloured in green, you will notice that a tooltip pops up with information regarding the total profit that Zayo earns from that state as well as the total number of buildings Zayo has in that state. Clicking any of the coloured states will scroll the view down to a datatable that consists of more information regarding Zayo's buildings in the corresponding state, such as the Building ID, Estimated build cost, profits as well as the exact address of a given building ID. A user can sort the datatable with any column as a key by clicking on the up and down arrows near the column name. If a user wishes to search for a particular keyword, he/she may type it into the search box located at the top-right corner of the data table.

  - The third visualization, titled Zayo' Portfolio, uses a tree-map to display the relative distribution of Zayo network across different industries and their corresponding verticals.

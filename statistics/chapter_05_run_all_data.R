source("utils_data.R")
source("utils_plots.R")

rexam <- getBookDataFile("rexam.dat")

# Clean Data
rexam$uni <- factor(rexam$uni, levels = c(0:1), labels = 
                      c("Duncetown University", "Sussex University"))
##

summary(rexam)

## Plots
histList <- lapply(names(rexam)[1:4], FUN = plotNumColDensity, rexam)

histList

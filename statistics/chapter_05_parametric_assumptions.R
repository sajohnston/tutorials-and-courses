library(car)
library(ggplot2)
library(pastecs)
library(psych)

source("utils_data.R")
source("utils_plots.R")

dlf <- getBookDataFile("DownloadFestivalNoOut.dat")

## Looking at histograms to see normality
hist.day1 <- plotDensity(dlf, "day1", "Hygiene score on day 1")
hist.day1 + addNormalCurve(dlf$day1, na.rm = TRUE)

hist.day2 <- plotDensity(dlf, "day2", "Hygiene score on day 2")
hist.day2 + addNormalCurve(dlf$day2, na.rm = TRUE)

hist.day3 <-plotDensity(dlf, "day3", "Hygiene score on day 3")
hist.day3 + addNormalCurve(dlf$day3, na.rm = TRUE)


## Looking at Q-Q plots to see normality

## The book says to use qplot with stat = "qq" but the stat arg is deprecated
qqplot.day1 <- qplot(sample = dlf$day1)
qqplot.day1

qqplot.day1 <-   ggplot(dlf, aes(sample = dlf$day1)) + stat_qq() 
qqplot.day1

qqplot.day2 <- ggplot(dlf, aes(sample = dlf$day2)) + stat_qq() 
qqplot.day2

qqplot.day3 <- ggplot(dlf, aes(sample = dlf$day3)) + stat_qq() 
qqplot.day3

## Quantify the shape of the distributions

### 'describe' in the Psych package
describe(dlf$day1)

### stat.desc in pastecs, turning off other options and including normal dist info
stat.desc(dlf$day1, basic = FALSE, norm = TRUE)

### Combined
describe(dlf[,c(3:5)])
stat.desc(dlf[,c(3:5)], basic = FALSE, norm = TRUE)

### Cleans up the output to something more visually appealing:
round(stat.desc(dlf[,c(3:5)], basic = FALSE, norm = TRUE), digits = 3)

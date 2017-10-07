dataLoc <- "C:\\Users\\sarah\\OneDrive\\Documents\\DiscoveringStatisticsR\\Data\\"

getBookDataFile <- function(fileName, header = TRUE){
 df <- read.delim(file.path(dataLoc, fileName, fsep = "\\"), header)
 return(df)
}
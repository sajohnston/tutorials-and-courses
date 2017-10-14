library(ggplot2)

plotDensity <- function(df, dataCol, label, ...){
  ggplot(df, aes(df[,dataCol])) +
    geom_histogram(aes(y = ..density..), colour = "black"
                   , fill = "white") + 
    labs(x = label, y = "Density")
}


addNormalCurve <- function(dataCol, ...){
  stat_function(fun = dnorm, 
                args = list(mean = mean(dataCol, ...),
                            sd = sd(dataCol, ...)),
                colour = "black",
                size = 1)
}

## This should check the column type, but doesn't currently
plotNumColDensity <- function(colName, df, label = NULL, 
                              normalCurve = TRUE, ...){
  
  if (is.null(label)){
    label <- colName
  }
  
  hist <- plotDensity(df, colName, label)
  if (normalCurve){
    hist <- hist + addNormalCurve(df[,colName], na.rm = TRUE)
  }
  
  hist
  
}
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
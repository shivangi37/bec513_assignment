library(ggplot2)

args <- commandArgs(trailingOnly = TRUE)
output_file <- args[1]            
x_label <- args[2]                  
y_label <- args[3]                 
plot_title <- args[4]    

data <- read.table("data2.tsv", header = FALSE, col.names = c("X", "Y", "Category"))

plot <- ggplot(data, aes(x = X, y = Y, color = Category, group = Category)) +
  geom_line(size = 1) +              
  labs(title = plot_title,            # Use command line for these
       x = x_label,                   
       y = y_label) +                
  theme_bw()

ggsave(output_file, plot = plot, width = 8, height = 6)


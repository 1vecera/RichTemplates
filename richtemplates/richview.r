# Install ggplot2 if not already installed
if (!requireNamespace("ggplot2", quietly = TRUE)) {
  install.packages("ggplot2")
}


# Load ggplot2 package
library(ggplot2)
windowsFonts(A = windowsFont("Palatino Linotype"))

richview_theme <- function() {
  theme(
    plot.background = element_rect(fill = "#FAF9F6"),
    panel.background = element_rect(fill = "#FAF9F6"),
    panel.grid.major.x = element_blank(),
    panel.grid.major.y = element_line(color = "#CCC1B7", size = 0.2),
    panel.grid.minor = element_blank(),
    axis.ticks.x = element_line(color = "#4D4845", size = 0.2),
    axis.ticks.y = element_blank(),
    axis.text.x = element_text(color = "#4D4845", size = 9.6, family = "A"),
    axis.text.y = element_text(color = "#4D4845", size = 9.6, family = "A"),
    axis.title.x = element_text(color = "#4D4845", size = 10.8, family = "A"),
    axis.title.y = element_text(color = "#4D4845", size = 10.8, family = "A"),
    legend.background = element_rect(fill = "#FAF9F6"),
    legend.key =  element_rect(fill = "#FAF9F6"),
    legend.position = c(0, 1.05),
    legend.justification = c(0, 1),
    legend.direction = "horizontal",
    legend.title = element_blank(),
    legend.text = element_text(size = 9.6, family = "A"),
    plot.title = element_text(size = 14.4, hjust = 0, family = "A"),
    plot.margin = margin(60, 60, 60, 60)
  )
}

data(mtcars)
p <- ggplot(mtcars, aes(x = mpg, y = disp, color = factor(cyl))) +
  geom_point() +
  labs(title = "Example Plot", x = "Miles per Gallon", y = "Displacement") +
  scale_color_manual(values = c("#186cac", "#81e7cc", "#eec8f1", "#dce475", "#86ec5a", "#eb70d5", "#829951", "#5a3386", "#a50fa9", "#4ba40b")) +
  richview_theme()


p


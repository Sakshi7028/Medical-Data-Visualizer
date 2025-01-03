from medical_data_visualizer import draw_cat_plot, draw_heat_map
import unittest
import test_module

# Generate and save categorical plot
cat_plot = draw_cat_plot()
cat_plot.savefig('catplot.png')
print("Categorical plot saved as 'catplot.png'.")

# Generate and save heat map
heat_map = draw_heat_map()
heat_map.savefig('heatmap.png')
print("Heatmap saved as 'heatmap.png'.")

# Run unit tests
print("\nRunning unit tests...\n")
unittest.TextTestRunner().run(unittest.defaultTestLoader.loadTestsFromModule(test_module))

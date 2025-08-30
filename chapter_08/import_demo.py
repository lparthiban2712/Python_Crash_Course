import flower
print(flower.flower_name('rose', 'lily', 'tulip'))  # Example usage

from flower import flower_name
print(flower_name('rose', 'lily', 'tulip'))  # Example usage

import flower as fl
print(fl.flower_name('rose', 'lily', 'tulip'))  # Example usage

from flower import flower_name as fn
print(fn('rose', 'lily', 'tulip'))  # Example usage

from flower import *
print(flower_name('rose', 'lily', 'tulip'))  # Example usage

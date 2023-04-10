import matplotlib.pyplot as plt

def generate_bar_chart(labels, values):
  fig, ax = plt.subplots()
  ax.set_ylabel('Raiting', color='black', )
  ax.set_xlabel('Tipo de cannabis', color ='green', fontsize= 20 )
  ax.bar(labels, values, width = 0.8, bottom = 0.1, edgecolor = "black", color = 'gray', facecolor='khaki')
  ax.set_title('Raiting de tipo de Cannabis', fontsize=20)
  plt.show()

def generate_pie_chart(labels, values):
  colores = ['green', 'gray', 'blue']
  fig, ax = plt.subplots()
  ax.pie(values, labels= labels, autopct='%.1f%%', colors = colores, shadow = True, startangle=90)
  ax.axis('equal')
  plt.show()

if __name__ == '__main__':
  labels = ['a', 'b', 'c']
  values = [10, 40, 800]
  # generate_bar_chart(labels, values)
  generate_pie_chart(labels, values)
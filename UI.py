import customtkinter
import matplotlib.pyplot as plt
import networkx as nx
from PIL import Image
import datetime

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

# Главное окно
root = customtkinter.CTk()
root.geometry("1000x750")

# frame с 1 заданием
frame1 = customtkinter.CTkFrame(master = root)
frame1.pack(pady = 20, padx = 60,side = 'left', fill = "both")


frame2 = customtkinter.CTkFrame(master = root)
frame2.pack(pady = 20, padx = 60,side = 'top', fill = "both")

date_frame = customtkinter.CTkFrame(master = frame1)
date_frame.pack(padx = '20',side = "top", fill = 'x')

# Начальную и конечную дату
start_date = datetime.date(2022, 12, 1)
end_date   = datetime.date(2023, 12, 1)

# Интервал между датами
interval   = datetime.timedelta(days=7)

dates = []
while start_date <= end_date:
    tempday = start_date
    start_date += interval
    dates.append(str(tempday.strftime('%d.%m.%Y')) + " - " + str(start_date.strftime('%d.%m.%Y')))


def set_Week(value):
    weekNumber = dates.index(value)
    TimeSlider.set(weekNumber)
    TimeLabel.configure(text = weekNumber)

def set_Date(value):
    week_combo.set(dates[int(value)])
    TimeLabel.configure(text = int(value))

TimeSlider = customtkinter.CTkSlider(master = date_frame, from_= 1, to= 52,command = set_Date)
TimeSlider.pack(side = 'left')
TimeSlider.set(1)

TimeLabel = customtkinter.CTkLabel(master = date_frame,text = '1')
TimeLabel.pack(side = 'left')


week_combo = customtkinter.CTkComboBox(master = date_frame, values= dates, width=180, command = set_Week)
week_combo.pack(pady = 10, padx = 10)



# Создаем граф
G = nx.DiGraph()

# Добавляем вершины и ребра
G.add_nodes_from([])
G.add_edges_from([])

# Настраиваем параметры отрисовки
pos = nx.spring_layout(G)  # Вычисляем позиционную информацию
node_size = 100  # Размер вершин
node_color = 'r'  # Цвет вершин

# Отрисовываем граф
nx.draw_networkx_nodes(G, pos, nodelist=list(G.nodes()), node_size=node_size, node_color=node_color)
nx.draw_networkx_edges(G, pos, edgelist=list(G.edges()), edge_color='b', width=2)

plt.savefig('graph/graph.png')  # Сохраняем граф в файл graph.


image_path = 'graph/graph.png'
image = customtkinter.CTkImage(light_image =Image.open(image_path), size = (700,700))
image_label = customtkinter.CTkLabel(master = frame1, image = image, text = '')
image_label.pack(pady = 10, padx = 12)


day_labels = ["Mon", "Tue", "Wed", "Four", "Fri", "Sun", "Sut"]
def generate():


    G.add_nodes_from(['D', 'E', 'F',])
    G.add_edges_from([('D', 'E'), ('E', 'F')])
        

    # Настраиваем параметры отрисовки
    pos = nx.spring_layout(G)  # Вычисляем позиционную информацию
    node_size = 100  # Размер вершин
    node_color = 'r'  # Цвет вершин

    # Отрисовываем граф
    nx.draw_networkx_nodes(G, pos, nodelist=list(G.nodes()), node_size=node_size, node_color=node_color)
    nx.draw_networkx_edges(G, pos, edgelist=list(G.edges()), edge_color='b', width=2)

    plt.savefig('graph/graph.png')  # Сохраняем граф в файл graph.


    image_path = 'graph/graph.png'
    image = customtkinter.CTkImage(light_image =Image.open(image_path), size = (700,700))
    image_label.configure(image = image)


button = customtkinter.CTkButton(master = frame1, text = "generate graph", command = generate)
button.pack(pady = 20)
    

root.mainloop()


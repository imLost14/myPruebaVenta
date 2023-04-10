import func
import read_ranking
import charts



if __name__ == '__main__':
    data = read_ranking.ranking_csv('/home/hector/pruebaPython/myPruebaVenta/universities_ranking.csv')
    universities, students = func.get_Cantidades(data)
    charts.generate_pie_chart(universities, students)
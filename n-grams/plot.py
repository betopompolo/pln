from collections import OrderedDict
from datetime import datetime

import matplotlib.pyplot as plt


def plot_results(results: dict[str, float]):
    dates = list(results.keys())
    dates.sort(key=lambda date: datetime.strptime(date, '%d/%m/%Y'))
    ordered_dict = OrderedDict()
    for date_str in dates:
        ordered_dict[date_str] = results[date_str]

    x = [date_str[:5] for date_str in ordered_dict.keys()]
    y = list(ordered_dict.values())

    plt.scatter(x, y)
    plt.xlabel('Data de publicação')
    plt.ylabel('Perplexidade')
    plt.title('Textos da Folha de São Paulo publicados no ano de 1994')
    plt.show()

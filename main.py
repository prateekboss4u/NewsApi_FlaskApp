
from flask import Flask, render_template, jsonify, json
from newsapi import NewsApiClient
from translate import Translator





app = Flask(__name__)


@app.route('/')
def bbc():
    newsapi = NewsApiClient(api_key="c3a1c7b45cd54460a87ea073582e486e")
    topheadlines = newsapi.get_top_headlines(sources="bbc-news")

    articles = topheadlines['articles']
    translator= Translator(to_lang='fr')
    obj = []
    for i in range(len(articles)):
        myarticles = articles[i]

        
        fr_description = translator.translate(myarticles['description'])
        fr_title = translator.translate(myarticles['title'])
        obj.append({'title_en': myarticles['title'], 
                    'desc_en': myarticles['description'] , 
                    "image_url": myarticles['urlToImage'],
                    'timestamp': myarticles['publishedAt'],
                    'title_fr': (fr_title),
                    'desc_fr': (fr_description)
                    })
    
    
    return jsonify({'news': obj})



if __name__ == "__main__":
    app.run(debug=True)
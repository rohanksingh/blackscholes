from flask import Flask, render_template, request
from oopimplementation import BsOption

app= Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def index():
    if request.method == 'POST':
        S= float(request.form['S'])
        K= float(request.form['K'])
        T= float(request.form['T'])
        r= float(request.form['r'])
        sigma= float(request.form['sigma'])
        option_type= request.form['type']
        
        # Instantiate the BsOption class
        
        option= BsOption(S, K, T, r, sigma)
        option_prices= option.price(option_type)
        
        return render_template('index.html', option_prices= option_prices)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)











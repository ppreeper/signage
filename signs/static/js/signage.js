    var sign = {
        getWeather: function(fn) {
            //$.get("https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%3D8676%20and%20u%3D'c'&format=json&callback=", function(data, status) {
            $.get("/media/weather.json", function(data, status) {
                var html = "";
                var ds = '<div>';
                var de = '</div>';
                var pnt = '<p class="newstitle">'
                var pn = '<p class="news">'
                var pe = '</p>'
                var units = data.query.results.channel.units;
                var location = data.query.results.channel.location;
                var wind = data.query.results.channel.wind;
                var atmosphere = data.query.results.channel.atmosphere;
                var astronomy = data.query.results.channel.astronomy;
                var title = data.query.results.channel.item.title;
                var condition = data.query.results.channel.item.condition;
                var forecast = data.query.results.channel.item.forecast;
                console.log(condition);
                html += ds
                html += pnt + "Conditions for " + location.city + pe
                html += pn
                html += condition.text + '<br>'
                html += condition.temp + '&deg' + units.temperature + '<br>'
                html += 'As of:' + condition.date
                html += pe
                html += de
                flen = forecast.length;
                for (i = 0; i < flen; i++){
                  html += ds
                  html += pnt
                  html += location.city + '<br>Forecast for <br>'
                  html += forecast[i].day +' '+forecast[i].date
                  html += pe
                  html += pn
                  html += 'High of ' + forecast[i].high + '&deg' + units.temperature + '<br>'
                  html += 'Low of ' + forecast[i].low + '&deg' + units.temperature + '<br>'
                  html += '<br>' + forecast[i].text + '<br>'
                  html += pe
                  html += de
                }

                // var ts = '<div>';
                // var te = '</div>';
                // var dlen = Object.keys(data['data']).length;
                // for (i = 0; i < dlen; i++) {
                //     // img_html += ts + '\n' + '<img class="image-item" src="' + data['data'][i]['src'] + '" alt="' + data['data'][i]['alt'] + '">' + '\n' + te + '\n';
                //     console.log(data[])
                // }
                console.log(html);
                fn(html);
            });

        }
    }

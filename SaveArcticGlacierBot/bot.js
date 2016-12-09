console.log('SaveTheArcticGlacier start..');

// Require twit NPM module 
var Twit = require('twit');

// Require config.js API key
var config = require('./config');

var T = new Twit(config);

k = 0;
n = 0;

// Require fs NPM module 
var fs = require('fs');

tweetIt();
// Set interval every 30 minutes
setInterval(tweetIt, 1000 * 60 * 30);

function tweetIt() {

    k = k + 10300;
    n = n + 1;

    var filename = 'test/img-' + n + '.jpg';
    var params = {
        encoding: 'base64'
    }
    var b64 = fs.readFileSync(filename, params);
    // Upload image
    T.post('media/upload', { media_data: b64 }, uploaded);

    function uploaded(err, data, response) {
        var id = data.media_id_string;
        var tweet = {
            status: '#SaveTheArcticGlacier just saved ' + k + ' square kilometers of the #arctic #glacier!!!',
            media_ids: [id]
        }
        T.post('statuses/update', tweet, tweeted);

    }

    function tweeted(err, data, response) {
        if (err) {
            console.log("Error!");
        } else {
            console.log("works..");
        }
    }

}

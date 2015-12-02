module.exports = {
  entry : './app-client.js',
  output: {
    path: "./app/static/js",
    filename: "bundle.js"
  },
  module: {
    loaders: [
      { test: /\.(woff|woff2)(\?v=\d+\.\d+\.\d+)?$/, 
        loader: 'url?limit=10000&mimetype=application/font-woff' },
      { test: /\.ttf(\?v=\d+\.\d+\.\d+)?$/, 
        loader: 'url?limit=10000&mimetype=application/octet-stream'},
      { test: /\.eot(\?v=\d+\.\d+\.\d+)?$/, 
        loader: 'file'},
      { test: /\.svg(\?v=\d+\.\d+\.\d+)?$/, 
        loader: 'url?limit=10000&mimetype=image/svg+xml'},
      { test: /\.css$/, loader: "style!css!" },
      {
				test: /^((?!config).)*\.js?$/,
        exclude: /(app-server.js)/,
        loaders: ["babel"],
      }
    ]
  }

};

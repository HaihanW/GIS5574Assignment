
var layer = new MapImageLayer({
  url:"https://sampleserver6.arcgisonline.com/arcgis/rest/services/Census/MapServer",
  sublayers: [
    {
      id: 10,
      renderer: {
        type: "class-breaks"
      },
      source: {
        mapLayerId: 1
      }
    },
    {
      id: 11,
      renderer: {
        type: "unique-value"
      },
      definitionExpression: "POP07_SQMI >= 5100",
      source: {
        mapLayerId: 1
      }
    },
    {
      id: 12,
      renderer: {
        type: "simple"
      },
      definitionExpression: "POP07_SQMI >= 5100",
      source: {
        mapLayerId: 1
      }
    }
  ]
});


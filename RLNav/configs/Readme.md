[
    {
        "type": "dense",
        "size": 32
    },
    {
        "type": "dense",
        "size": 32
    },
    {
        "type": "lstm",
        "size": 512,
	"dropout": "None" <-- Specifies interconnetion, 0 no dropout, 1 no connection
    }
]

Dropout: Umbedingt aktivieren:
https://www.quora.com/In-Keras-what-is-a-dense-and-a-dropout-layer

In contrast to the dropout layer, a dense layer is simply a layer where each unit or neuron is connected to each neuron in the next layer.

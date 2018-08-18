# SensoGlove

Python wrapper module to interact with [SensoGloves](https://senso.me/).

It handles for you the socket connection and the raw payload parsing, only leaving to you the fun parts of the job !

## Installation

`$ pip install sensoglove`

## Usage

Import the SensoGlove class in your python code

```python
from sensoglove import SensoGlove
```

Then, instantiate a new SensoGlove object and connect

```python
glove = SensoGlove('127.0.0.1', 53451)
glove.connect()
```

Now, you just have to create a loop to continuously fetch data from gloves and the data is yours !

```python
while 1:
    gloves.fetch_data()
    print(gloves.hand.fingers.index.pinch)
    print(gloves.hand.fingers.middle.pinch)
    print(gloves.hand.fingers.third.pinch)
    print(gloves.hand.fingers.little.pinch)
```

## Documentation

### SensoGlove(host, port)

* `host` {`String`} - Glove's listener host
* `port` {`Integer`} - Glove's listener port

#### Properties

* `host` {`String`} - Host passed in
* `port` {`Integer`} - Port passed in
* `src` {`String`} - Glove's source mac address
* `name` {`String`} - Glove's name
* `battery` {`Integer`} - Glove's battery level
* `temperature` {`Integer`} - Glove's temperature

* `hand` {`Hand Object`} - Hand Object containing hand's informations

#### Methods

* `connect()` - Connect the script to the glove
* `fetch_data()` - Fetch data to be parsed by the module. (Has to be put in a loop, so the fetching is continuous)
* `send_vibration(fingers, [duration], [strength])`
  * `fingers` {`List of String`} - List of fingers you want to vibrate
  * `duration` {`Integer`} - Duration of the vibration <0-65536>
  * `strength` {`Integer`} - Strength of the vibration <0 - 10>

### Hand

#### Properties

* `type` {`String`} - Hand type (`lh`/`rh` for left-hand/right-hand)
* `palm` {`Palm Object`} - Palm Object containing palm's informations
* `wrist` {`Wrist Object`} - Wrist Object containing wrist's informations
* `fingers` {`Fingers Object`} - Fingers Object containing fingers' informations

### Palm

#### Properties

* `rotation` {`Rotation Object`} - Rotation of the Palm
* `speed` {`Speed Object`} - Speed of the Palm
* `acceleration` {`Speed Object`} - Acceleration of the Palm
* `data` {`Dictionary`} - Raw Palm data (shouldn't be needed)

### Speed

#### Properties

* `x` {`Integer`} - Speed/Acceleration on x axis
* `y` {`Integer`} - Speed/Acceleration on y axis
* `z` {`Integer`} - Speed/Acceleration on z axis

### Wrist

#### Properties

* `rotation` {`Rotation Object`} - Rotation of the Wrist
* `data` {`Dictionary`} - Raw Wrist data (shouldn't be needed)

### Fingers

#### Properties

* `thumb` {`Thumb Object`} - Thumb Object containing Thumb informations
* `middle` {`Rotation Object`} - Rotation of the middle finger
* `third` {`Rotation Object`} - Rotation of the third finger
* `little` {`Rotation Object`} - Rotation of the little finger
* `data` {`Dictionary`} - Raw Fingers data (shouldn't be needed)

#### Notes

Roll property is not set in Rotation Object that represent finger rotation, as usually human cannot rotate finger in that axis.

### Thumb

* `rotation` {`Rotation Object`} - Rotation of the thumb
* `bend` {`Integer`} - Bending of the distal phalanx of the thumb


### Rotation

#### Properties

* `pitch` {`Integer`} - Pitch Rotation
* `roll` {`Integer`} - Roll Rotation (not set for finger representation)
* `yaw` {`Integer`} - Yaw Rotation

## Useful links

* [Gloves raw network protocol](https://senso.me/docs/net_protocol/)

## Contributing

See something that could be improved ? [Open an issue](https://github.com/TheRizzen/sensogloves/issues/new) or contribute !

* Fork it
* Create your feature branch
* Commit your changes and push them to your branch
* Create a new Pull Request

## License

MIT

import QtQuick 2.0
import Sailfish.Silica 1.0
import Nemo.KeepAlive 1.2

import QtMultimedia 5.6

import org.nubecula.harbour.hafenschau 1.0

Page {
    property bool playing: true
    property string url

    id: page

    allowedOrientations: Orientation.All

    DisplayBlanking { preventBlanking: true }

    SilicaFlickable {
        anchors.fill: parent

        Rectangle {
            anchors.fill: parent
            color: "black"
        }

        MediaPlayer {
            id: videoPlayer
            source: url
            autoPlay: true
        }

        VideoOutput {
            anchors.fill: parent
            source: videoPlayer

            Image {
                visible: !playing
                anchors.centerIn: parent
                source: "image://theme/icon-l-play"
            }

            Slider {
                id: seekSlider
                anchors.bottom: parent.bottom
                width: parent.width
                minimumValue: 0
                maximumValue: videoPlayer.duration
                stepSize: 1000
                value: videoPlayer.position

                onExited: videoPlayer.seek(value)
            }
        }

        MouseArea {
            id: playArea
            anchors.top: parent.top
            width: parent.width
            height: parent.height - seekSlider.height

            onPressed: {
                if (playing) {
                    playing = false;
                    videoPlayer.pause();
                } else {
                    playing = true;
                    videoPlayer.play();
                }
            }

        }
    }
}


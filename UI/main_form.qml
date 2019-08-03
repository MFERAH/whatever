import QtQuick 2.3
import QtQuick.Controls 2.3
import QtQuick.Window 2.3
import QtQuick.Layouts 1.13

ApplicationWindow{

    menuBar:MenuBar{

    Menu{
        title: qsTr("File")
        MenuItem{
            text: qsTr("Open Description File:")
        }
    }

    Menu{
        title:  qsTr("About")
        MenuItem{
            text: qsTr("About ...")
        }
    }
    }

    header: TabBar{

    }

    footer: ToolBar{

    }

    GridLayout{

        ListView{//the list view for modules

        }

/*
idk wtf here (main editor)
*/

        StackLayout{//property panel

        }

    }
}


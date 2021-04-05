import { StatusBar } from 'expo-status-bar';
import React from 'react';
import { StyleSheet, Text, View, FlatList, Image, Dimensions } from 'react-native';
import { SafeAreaView } from "react-native-safe-area-context";


const DATA = [
  {
    id: 'bd7acbea-c1b1-46c2-aed5-3ad53abb28ba',
    title: 'Pic',
  },
  {
    id: '3ac68afc-c605-48d3-a4f8-fbd91aa97f63',
    title: 'Pic',
  },
  {
    id: '58694a0f-3da1-471f-bd96-145571e29d72',
    title: 'Pic',
  },
];


function Picture(props) {
  return (
    <View style={styles.imgContainer}>
      <Image
        style={styles.imgPicture}
        source={{
          uri: 'https://reactnative.dev/img/tiny_logo.png',
        }}
      />
      <Text>{props.title}</Text>      
    </View>
  )
}

export default function App() {


  const renderPic = ({ item }) => (
    <Picture title={item.title} />
  );


  return (
    <SafeAreaView style={styles.container}>
      <StatusBar style="auto" />
      <View style={styles.header}>
        <Text>[pasta-icon] [####-----------]</Text>        
      </View>
      <FlatList
        style={styles.lineContainer}
        data={DATA}
        renderItem={renderPic}
        keyExtractor={item => item.id}
        numColumns={3}
      />
    </SafeAreaView>
  );
}

var width = Dimensions.get('window').width; //full width

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: "center",
  },
  header: {
    margin: 10,
    padding: 15,
    borderRadius: 10,
    alignItems: "center",
    backgroundColor: "grey",
    width: "90%",
  },
  lineContainer: {
    width: width,    
  },
  imgContainer: {
    alignItems: "center",
    justifyContent: 'space-between',
    flexGrow: 1,
    margin: 5,
    borderWidth: 1,
    borderColor: 'black',
    borderStyle: 'solid',
  },
  imgPicture: {
    width: "100%",
    height: 110,
  },
});

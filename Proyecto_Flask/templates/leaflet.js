import React, { Component } from "react";
import Leaflet from "react-leaflet";

class App extends Component {
  render() {
    return (
      <Leaflet>
        <Map center={[0, 0]} zoom={2} />
      </Leaflet>
    );
  }
}
import React from 'react';

import SearchBar from '../components/SearchBar';
import NavigationBarHome from '../components/NavigationBarHome';

const HomeScreen = () => {

    return (
      <div style={{display: 'flex', flexDirection: 'column'}} > 
        <NavigationBarHome style={{ alignSelf: 'start' }} ></NavigationBarHome>
        <SearchBar></SearchBar>
      </div>
    )
  }
  
export default HomeScreen;
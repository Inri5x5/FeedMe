import React from 'react';

import SearchBar from '../components/SearchBar';
import NavigationBarHome from '../components/NavigationBarHome';
import SelectedIngredientLabel from '../components/SelectedIngredientLabel';

const HomeScreen = () => {

    return (
      <div style={{display: 'flex', flexDirection: 'column'}} > 
        <NavigationBarHome style={{ alignSelf: 'start' }} isLogin={false} ></NavigationBarHome>
        <SearchBar style={{ margin: '100px' }}></SearchBar>
        {/* <SelectedIngredientLabel></SelectedIngredientLabel> */}
      </div>
    )
  }
  
export default HomeScreen;
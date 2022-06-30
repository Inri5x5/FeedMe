import React from 'react';

import SearchBar from '../components/SearchBar';
import NavigationBarHome from '../components/NavigationBarHome';
import FilterContainer from '../components/FilterContainer';

const HomeScreen = () => {
    const [selectedIngredients, setSelectedIngredients] = React.useState([]);
    const [selectedTags, setSelectedTags] = React.useState([]);
    
    return (
      <div style={{display: 'flex', flexDirection: 'column'}} > 
        <NavigationBarHome style={{ alignSelf: 'start' }} ></NavigationBarHome>
        <SearchBar style={{ marginTop: '30px' }} 
          selectedIngredients={selectedIngredients}
          setSelectedIngredients={setSelectedIngredients}
        />
        <FilterContainer
          selectedTags={selectedTags}
          setSelectedTags={setSelectedTags} 
        />
      </div>
    )
  }
  
export default HomeScreen;
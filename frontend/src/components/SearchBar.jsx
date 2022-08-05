import React from 'react'
import { useState } from 'react';
import { APICall } from '../helperFunc';
import KeyboardArrowDownIcon from '@mui/icons-material/KeyboardArrowDown';
import styles from './styles/SearchBar.module.css'
import textStyles from './styles/SearchBarTitle.module.css'
import SearchIcon from '@mui/icons-material/Search';
import CategoryLabel from './CategoryLabel';
import IngredientLabel from './IngredientLabel';
import SelectedIngredientLabel from './SelectedIngredientLabel';
import ArrowBackIcon from '@mui/icons-material/ArrowBack';
import { IconButton } from '@mui/material';
import DeleteIcon from '@mui/icons-material/Delete';
import homeChef from '../assets/homeChef.png'

const SearchBar = (props) => {
  // Data State
  const [listIngredient, setListIngredient] = useState([]);
  const [listCategories, setListCategories] = useState([]);

  const getAllCategories = async() => {
    let data = []; let temp = [];
    try {
      const headers = {
        'Content-Type': 'application/json',
      };
      data = await APICall(null, '/categories', 'GET', headers);
      for (let i = 0; i < data.body.categories.length; i++) {
        temp.push({"c_id": data.body.categories[i].c_id, "name": data.body.categories[i].name})
      }
      setListCategories(temp);
    } catch (err) {
      alert(err);
    }
  }
  const getAllIngredients = async() => {
    let data = []; let temp = [];
    try {
      const headers = {
        'Content-Type': 'application/json',
      };
      data = await APICall(null, `/ingredients?query= `, 'GET', headers);
      for (let i = 0; i < data.body.suggestions.length; i++) {
        temp.push({"i_id": data.body.suggestions[i].i_id, "name": data.body.suggestions[i].name, "c_id": data.body.suggestions[i].c_id})
      }
      setListIngredient(temp);
    } catch (err) {
      alert(err);
    }
  }

  //Dropdown Features
  //There will be 2 state in regards to open dropdown
  //1. Showing Categories
  //2. Showing Ingredient
  //3. Showing Searches
  const [dropdownState, setDropdownState] = useState('Category');
  const [showDropdown, setDropdown] = useState(false);

  const clickDropdown = () => {
    if (showDropdown === true) {
      setDropdown(false)
    }
    showDropdown ? setDropdown(false) : setDropdown(true);
  }
  const handleBlur = (event) => {
    if (!event.currentTarget.contains(event.relatedTarget)) {
      setDropdown(false)
    }
  }
  const backToCategory = () => {

    setCategory({"c_id": -1, "name": "Category"});
    setDropdownState("Category")
  }
  const renderBackIcon = () => {
    return (
      <div className={styles.back_button} onClick={() => backToCategory()}>
        <ArrowBackIcon></ArrowBackIcon>
      </div>
    )
  }

  //Category Feature
  const [category, setCategory] = useState({"c_id": -1, "name": "Category"});
  const renderCategory = (list_categories) => {
    let content = list_categories.map((object, index) => {
      return (<CategoryLabel object={object} setMenuName={setCategory} setDropdownState={(input === '') ? () => setDropdownState("Ingredient") : () => setDropdownState("Searches")}></CategoryLabel>)
    })
    return content;
  }

  //Ingredient Feature
  const renderIngredient = (list_ingredients) => {
    let content = list_ingredients.map((object, index) => {
      const isSelected = checkIfSelected(object);
      return (<IngredientLabel object={object} isSelected={isSelected} clickFunction={isSelected ? removeIngredientOnClick : addIngredientOnClick}></IngredientLabel>)
    })
    return content;
  }
  const addIngredientOnClick = (object) => {
    props.setSelectedIngredients([...props.selectedIngredients, object]);
  }
  const removeIngredientOnClick = (object) => {
    props.setSelectedIngredients(props.selectedIngredients.filter(selIngr => {
      return selIngr.i_id !== object.i_id;
    }))
  }
  const removeAllIngredients = () => {
    props.setSelectedIngredients([])
  }
  const renderSelectedIngredient = (list_selected_ingredients) => {
    let content = list_selected_ingredients.map((object, index) => {
      return (<SelectedIngredientLabel object={object} removeIngredient={removeIngredientOnClick}></SelectedIngredientLabel>)
    })
    if (list_selected_ingredients.length > 0) content.push(
      <IconButton onClick={removeAllIngredients} sx={{marginRight: '10px', backgroundColor:'red', color:'white', 
      '&:hover': {
        backgroundColor: "orange",
        color: "red"
      }}}>
        <DeleteIcon />
      </IconButton>
    )
    return content;
  }
  const checkIfSelected = (object) => {
    for(let i = 0; i < props.selectedIngredients.length; i++) {
      if (object.i_id === props.selectedIngredients[i].i_id) return true;
    }
    return false;
  }

  //Searching Feature
  const [input, setInput] = useState('');
  const [found, setFound] = useState([]);
  const onInput = (e) => {
    setInput(e.target.value);
    searchIngredient(e.target.value, listIngredient, category);
    if (e.target.value === "") {
      if (category.name !== "Category") {
        setDropdownState('Ingredient')
      } else {
        setDropdownState('Category');
      }
    } else {
      setDropdown(true);
      setDropdownState('Searches')
    }
  }
  const searchIngredient = (name, list_ingredients, category) => {
    let found = [];
    for (let i = 0; i < list_ingredients.length; i++) {
      if (category.name === "Category"){
        if (list_ingredients[i].name.toLowerCase().includes(name.toLowerCase())) {
          found.push(list_ingredients[i]);
        }
      } else {
        if (list_ingredients[i].name.toLowerCase().includes(name.toLowerCase()) && list_ingredients[i].c_id === category.c_id) {
          found.push(list_ingredients[i]);
        }
      }
    }
    setFound(found);
  }

  // Recommendation Ingredient Feature
  const [recommendedIngredients, setRecommendedIngredients] = React.useState('')

  const getRecommendedIngredients = async() => {
    let data = []; let temp = [];
    try {
      const headers = {
        'Content-Type': 'application/json',
      };
      data = await APICall(null, `/search/recommendation `, 'GET', headers);
      for (let i = 0; i < data.ingredients_list.length; i++) {
        temp.push({"i_id": data.ingredients_list[i].id, "name": data.ingredients_list[i].name})
      }
      setRecommendedIngredients(temp);
    } catch (err) {
      alert(err);
    }
  }

  const renderRecommendedIngredients = () => {
    let i = 0
    let index = 0
    let content = []
    while (i < 10 && index < recommendedIngredients.length) {
      if (!checkIfSelected(recommendedIngredients[index])) {
        content.push(
          <IngredientLabel object={recommendedIngredients[index]} isSelected={false} clickFunction={addIngredientOnClick}></IngredientLabel>
        )
        index++; i++;
      } else {
        index++
      }
    }
    return content
  }

  // Display Feature
  const renderSearchTitle = () => {
    return (
      <div style={{ width : "100%", marginBottom: "20px" }}>
        Searching for {input} in {(category.name === 'Category') ? "All Categories" : category.name}
      </div>
    )
  }
  const renderHomeTitle = () => {
    if (props.selectedIngredients.length === 0){
      return "Let's Start Cooking!"
    } else {
      return "Today I have"
    }
  }
  React.useEffect(() => {
    getAllCategories();
    getAllIngredients();
    getRecommendedIngredients();
  },[]);


  React.useEffect(() => {
    if ((dropdownState === 'Category') || (dropdownState === "Searches" && category.name === "Category")) {
      getAllIngredients();
    } else {
      searchIngredient(input, listIngredient, category);
    }
  },[dropdownState]);

  return (
    <>
      <div className={textStyles.container}>
        <div className={textStyles.wrapper}>
          <img style={{width: '30vw', aspectRatio:'1/1', objectFit:'cover'}} src={homeChef} alt="ChefHomeScreen"></img>
          <h1 className={textStyles}>
            {renderHomeTitle()}
          </h1>
        </div>
        <div className={styles.selected_ingredient_container}>
          {renderSelectedIngredient(props.selectedIngredients)}
        </div>
      </div>
      {(props.selectedIngredients.length > 0) && <div style={{textAlign:'center', marginTop: 15}}> 
        <span className={textStyles.num_recipes}>You can make {props.numRecipesFound} recipes </span> 
      </div>}
      {(props.selectedIngredients.length > 0) && <div style={{
        display:'flex', 
        width: '80vw', 
        justifyContent: 'flex-start', 
        alignItems:'center',
        marginLeft:'auto',
        marginRight:'auto',
        marginTop:'10px',
      }}>
        <div className={textStyles.recommended}>
          Did you have?
        </div>
        <div style={{display: 'flex', flexWrap:'wrap', marginLeft: 20}}>
          {renderRecommendedIngredients()}
        </div>
      </div>}
      <div className={styles.search_bar} onBlur={(e) => handleBlur(e)}>
        <div className={styles.search_category} >
          <div className={styles.search_category_link} tabIndex='0' onClick={() => clickDropdown()}>
            <span>{category.name}</span>
            <KeyboardArrowDownIcon className={showDropdown ? styles.search_category_icon_focus : styles.search_category_icon}/>
          </div>
          <div className={showDropdown ? styles.category_menu_focus : styles.category_menu} tabIndex='0'>
            { (dropdownState === 'Category') && renderCategory(listCategories) }
            { (dropdownState === 'Searches') && renderSearchTitle() }
            { (category.name !== 'Category') && renderBackIcon() }
            { (category.name === 'Category') && (dropdownState === "Searches") && renderBackIcon() }
            { (dropdownState === 'Ingredient') && renderIngredient(found) }
            { (dropdownState === 'Searches') && renderIngredient(found) }
          </div>
        </div>
        <div className={styles.input_search}>

          <input type="text" placeholder={"Search Your Ingredient " + ((category.name === 'Category') ? "" : "in " + category.name) } value={input} onInput={(e) => onInput(e)}/>
        </div>
        <a className={styles.search_btn}>
          <SearchIcon className={styles.search_btn_icon}></SearchIcon>
        </a>
      </div>
    </>


  )
}

export default SearchBar
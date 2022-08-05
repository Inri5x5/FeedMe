import React from 'react'
import { useEffect, useState } from 'react';
import KeyboardArrowDownIcon from '@mui/icons-material/KeyboardArrowDown';
import styles from './styles/SearchBarRecipe.module.css'
import CategoryLabel from './CategoryLabel';
import IngredientLabel from './IngredientLabel';
import ArrowBackIcon from '@mui/icons-material/ArrowBack';
import PropTypes from 'prop-types';

const SearchBarRecipe = (props) => {
    React.useEffect(() => { 
		let isFetch = true;
		function isEmpty(ob){
			for(var i in ob){ return false;}
		   return true;
		 }
        if(!isEmpty(props.preFilled)) {
			console.log('HEREE')
			console.log(props.preFilled)
			console.log(props.preFilled.name)
			setInput(props.preFilled.name)
        }
        return () => isFetch = false;
    }, [props, props.preFilled])
	
	//Dropdown Features
	//There will be 2 state in regards to open dropdown
	//1. Showing Categories
	//2. Showing Ingredient
	//3. Showing Searches
	const [dropdownState, setDropdownState] = useState('Category');
	const [showDropdown, setDropdown] = useState(false);
	
	//Searching Feature
	const [input, setInput] = useState('');
	const [found, setFound] = useState([]);
	
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
	const [selectedIngredients, setSelectedIngredients] = useState({}); 
	const renderIngredient = (list_ingredients) => {
		let content = list_ingredients.map((object, index) => {
			let isSelected = checkIfSelected(object);
		    if(props.preFilled !== {}) { isSelected = true }
			return (<IngredientLabel object={object} isSelected={isSelected} clickFunction={addIngredientOnClick}></IngredientLabel>)
		})
		return content;
	}
	
	const addIngredientOnClick = (object) => {
		console.log(object)
		setSelectedIngredients(object);
		setInput(object.name);
		props.updateIngredients(props.index, object);
	}

	const checkIfSelected = (object) => {
		if (object.ingredient_id === selectedIngredients.ingredient_id) return true;
		return false;
	}

	const onInput = (e) => {
		setInput(e.target.value);
		searchIngredient(e.target.value, props.listIngredient, category);
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
			if (!name) {name = ' '};
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
	const renderSearchTitle = () => {
		return (
			<div style={{ width : "100%", marginBottom: "20px" }}> 
				Searching for {input} in {(category.name === 'Category') ? "All Categories" : category.name}
			</div>
		)
	}

	React.useEffect(() => {
		searchIngredient(input, props.listIngredient, category);
	},[dropdownState]);
		
	return (
		<>
			<div className={styles.search_bar} onBlur={(e) => handleBlur(e)}>
				<div className={styles.search_category} >
					<div className={styles.search_category_link} tabIndex='0' onClick={() => clickDropdown()}>
						<span>{category.name}</span>
						<KeyboardArrowDownIcon className={showDropdown ? styles.search_category_icon_focus : styles.search_category_icon}/>
					</div>
					<div className={showDropdown ? styles.category_menu_focus : styles.category_menu} tabIndex='0'>
						{ (dropdownState === 'Category') && renderCategory(props.listCategories) }
						{ (dropdownState === 'Searches') && renderSearchTitle() }
						{ (category.name !== 'Category') && renderBackIcon() }
						{ (category.name === 'Category') && (dropdownState === "Searches") && renderBackIcon() }
						{ (dropdownState === 'Ingredient') && renderIngredient(found) }
						{ (dropdownState === 'Searches') && renderIngredient(found) }
					</div>
				</div>
				<div className={styles.input_search}>
					<input type="text" 
					    placeholder={"Search Your Ingredient " + ((category.name === 'Category') ? "" : "in " + category.name) } 
					    value={input} 
					    onInput={(e) => onInput(e)}/>
				</div>
			</div>
		</>
	

	)
}

SearchBarRecipe.propTypes = {
    updateIngredients: PropTypes.func,
    preFilled: PropTypes.object,
    index: PropTypes.number,
    listIngredient: PropTypes.array,
    listCategories: PropTypes.array
}

export default SearchBarRecipe
import React from 'react'
import { useEffect, useState } from 'react';
import KeyboardArrowDownIcon from '@mui/icons-material/KeyboardArrowDown';
import styles from './styles/SearchBar.module.css'
import textStyles from './styles/SearchBarTitle.module.css'
import SearchIcon from '@mui/icons-material/Search';
import CategoryLabel from './CategoryLabel';
import IngredientLabel from './IngredientLabel';
import SelectedIngredientLabel from './SelectedIngredientLabel';
import ArrowBackIcon from '@mui/icons-material/ArrowBack';

const SearchBar = () => {
	
	//Dropdown Features
	//There will be 2 state in regards to open dropdown
	//1. Showing Categories
	//2. Showing Ingredient
	//3. Showing Searches
	const [dropdownState, setDropdownState] = useState('Category');
	const [showDropdown, setDropdown] = useState(false);
	const resetDropdown = () => {
		setDropdown(false);
		setCategoryMenuName('Category');
		setDropdownState('Category')
	}
	const clickDropdown = () => {
		if (showDropdown === true) {
			// if (categoryMenuName !== "Category") {
			// 	setDropdown(false);
			// } else {
			// 	resetDropdown();
			// }
			setDropdown(false)
		}
		showDropdown ? setDropdown(false) : setDropdown(true);
	}
	const handleBlur = (event) => {
		if (!event.currentTarget.contains(event.relatedTarget)) {
			// if (categoryMenuName !== "Category") {
			// 	setDropdown(false);
			// } else {
			// 	resetDropdown();
			// }
			setDropdown(false)
		}
	}
	const backToCategory = () => {
		setCategoryMenuName("Category");
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
	const [categoryMenuName, setCategoryMenuName] = useState('Category');
	const renderCategory = (list_categories) => {
		let content = list_categories.map((name, index) => {
			return (<CategoryLabel text={name} setMenuName={setCategoryMenuName} setDropdownState={setDropdownState}></CategoryLabel>)
		})
		return content;
	}

	//Ingredient Feature
	const [selectedIngredients, setSelectedIngredients] = useState([]); 
	const renderIngredient = (list_ingredients) => {
		let content = list_ingredients.map((object, index) => {
			const isSelected = checkIfSelected(object);
			return (<IngredientLabel object={object} isSelected={isSelected} clickFunction={isSelected ? removeIngredientOnClick : addIngredientOnClick}></IngredientLabel>)
		})
		return content;
	}
	const addIngredientOnClick = (object) => {
		setSelectedIngredients([...selectedIngredients, object]);
	}
	const removeIngredientOnClick = (object) => {
		setSelectedIngredients(selectedIngredients.filter(selIngr => {
			return selIngr.id !== object.id;
		}))
	}
	const renderSelectedIngredient = (list_selected_ingredients) => {
		let content = list_selected_ingredients.map((object, index) => {
			return (<SelectedIngredientLabel object={object} removeIngredient={removeIngredientOnClick}></SelectedIngredientLabel>)
		})
		return content;
	}
	const checkIfSelected = (object) => {
		for(let i = 0; i < selectedIngredients.length; i++) {
			if (object.id === selectedIngredients[i].id) return true;
		}
		return false;
	}

	//Searching Feature
	const [input, setInput] = useState('');
	const [found, setFound] = useState([]);
	// const handleEnterKey = (event) => {
	// 	if (event.key === 'Enter') {
	// 		searchIngredient(input, ingredients);
	// 		setDropdownState('Searches');
	// 		setDropdown(true);
	// 	}
	// }
	const onInput = (e) => {
		setInput(e.target.value);
		searchIngredient(e.target.value, ingredients);
		if (e.target.value === "") {
			if (categoryMenuName !== "Category") {
				setDropdownState('Ingredient')
			} else {
				setDropdownState('Category');
			}
		} else {
			setDropdown(true);
			setDropdownState('Searches')
		}
	}
	const searchIngredient = (name, list_ingredients) => {
		let found = [];
		for (let i = 0; i < list_ingredients.length; i++) {
			if (list_ingredients[i].name.includes(name)) found.push(list_ingredients[i])
		}
		setFound(found);
	}
	const renderSearchTitle = () => {
		return (
			<div style={{ width : "100%", marginBottom: "20px" }}> 
				Searching for {input} in {(categoryMenuName === 'Category') ? "All Categories" : categoryMenuName}
			</div>
		)
	}

	//Dummy Data
	const categories = ['Vegetables', 'Fruits', 'Herbs & Spices', 'Pasta & Rice', 'Meat & Poultry', 'Seafood', 'Fats & Oils', 'Eggs & Dairy', 'Others']
	let ingredients = [{"id": -1, "name":'short name'}, {"id": -2, "name": "a reallyyyy longgg nameeeeeee of ingrreedient"}];
	for (let i = 0; i < 50; i ++) {
		ingredients.push({"id": i, "name": "Lorem Ipsum Ingre" + i});
	}
		
	return (
		<>
			<div className={textStyles.container}>
				<h1 className={textStyles} data-shadow="Today I have">Today I have</h1>
				<div className={styles.selected_ingredient_container}>
					{renderSelectedIngredient(selectedIngredients)}
				</div>
			</div>
			<div className={styles.search_bar} onBlur={(e) => handleBlur(e)}>
				<div className={styles.search_category} >
					<div className={styles.search_category_link} tabIndex='0' onClick={() => clickDropdown()}>
						<span>{categoryMenuName}</span>
						<KeyboardArrowDownIcon className={showDropdown ? styles.search_category_icon_focus : styles.search_category_icon}/>
					</div>
					<div className={showDropdown ? styles.category_menu_focus : styles.category_menu} tabIndex='0'>
						{ (dropdownState === 'Category') && renderCategory(categories) }
						{ (dropdownState === 'Searches') && renderSearchTitle() }
						{ (categoryMenuName !== 'Category') && renderBackIcon() }
						{ (categoryMenuName === 'Category') && (dropdownState === "Searches") && renderBackIcon() }
						{ (dropdownState === 'Ingredient') && renderIngredient(ingredients) }
						{ (dropdownState === 'Searches') && renderIngredient(found) }
					</div>
				</div>
				<div className={styles.input_search}>
					<input type="text" placeholder={"Search Your Ingredient " + ((categoryMenuName === 'Category') ? "" : "in " + categoryMenuName) } value={input} onInput={(e) => onInput(e)}/>
				</div>
				<a href="#" className={styles.search_btn}>
					<SearchIcon className={styles.search_btn_icon}></SearchIcon>
				</a>
			</div>
		</>
	

	)
}

export default SearchBar
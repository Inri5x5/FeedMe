import React from 'react'
import { useState } from 'react';
import KeyboardArrowDownIcon from '@mui/icons-material/KeyboardArrowDown';
import styles from './styles/SearchBar.module.css'
import textStyles from './styles/SearchBarTitle.module.css'
import SearchIcon from '@mui/icons-material/Search';
import CategoryLabel from './CategoryLabel';
import IngredientLabel from './IngredientLabel';
import SelectedIngredientLabel from './SelectedIngredientLabel';
import ArrowBackIcon from '@mui/icons-material/ArrowBack';

const SearchBar = (props) => {
	// Data State
	const [listIngredient, setListIngredient] = useState([]);
	const [listCategories, setListCategories] = useState([]);

	// General API-call boilerplate function
	const APICall = (requestBody, path, methodType, headersData) => {
		if (requestBody !== null) requestBody = JSON.stringify(requestBody);
		return new Promise((resolve, reject) => {
			const init = {
			method: methodType,
			headers: headersData,
			body: requestBody,
			}
			fetch(`${path}`, init)
			.then(response => {
				if (response.status === 200) {
				return response.json().then(resolve);
				} else if (response.status === 400) {
				return response.json().then(obj => {
					reject(obj.error);
				});
				} else {
				throw new Error(`${response.status} Error with API call`);
				}
			});
		})
	}

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
	const renderSelectedIngredient = (list_selected_ingredients) => {
		let content = list_selected_ingredients.map((object, index) => {
			return (<SelectedIngredientLabel object={object} removeIngredient={removeIngredientOnClick}></SelectedIngredientLabel>)
		})
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
	const renderSearchTitle = () => {
		return (
			<div style={{ width : "100%", marginBottom: "20px" }}> 
				Searching for {input} in {(category.name === 'Category') ? "All Categories" : category.name}
			</div>
		)
	}

	React.useEffect(() => {
		getAllCategories();
		getAllIngredients();
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
				<h1 className={textStyles} data-shadow="Today I have">Today I have</h1>
				<div className={styles.selected_ingredient_container}>
					{renderSelectedIngredient(props.selectedIngredients)}
				</div>
			</div>
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
				<a href="#" className={styles.search_btn}>
					<SearchIcon className={styles.search_btn_icon}></SearchIcon>
				</a>
			</div>
		</>
	

	)
}

export default SearchBar
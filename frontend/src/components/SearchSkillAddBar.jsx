import React from "react";
import SearchIcon from "@mui/icons-material/Search";
import CloseIcon from "@mui/icons-material/Close";
import styles from './styles/SearchSkillAddBar.module.css';
import PropTypes from 'prop-types';

function SearchSkillAddBar(props) {
	React.useEffect(() => { 
		let isFetch = true;
		if(props.preFilled !== {} && props.preFilled !== undefined ) {
				setWordEntered(props.preFilled.title)
		}
		return () => isFetch = false;
	}, [props])

	const [filteredData, setFilteredData] = React.useState([]);
	const [wordEntered, setWordEntered] = React.useState("");

	const handleFilter = (event) => {
		const searchWord = event.target.value;
		setWordEntered(searchWord);
		const newFilter = props.data.filter((value) => {
			return value.title.toLowerCase().includes(searchWord.toLowerCase());
		});

		if (searchWord === "") {
			setFilteredData([]);
		} else {
			setFilteredData(newFilter);
		}
	};

	const clearInput = () => {
		setFilteredData([]);
		setWordEntered("");
	};

	const handleChange = (value) => {
		setWordEntered(value.title);
		setFilteredData([]);
		const obj = {title: value.title, url: value.url, video_id: value.id}
		props.updateVideoSkill(obj, props.index);
	}
	return (
		<div className={styles.search}>
			<div className={styles.searchInputs}>
				<input
					type="text"
					placeholder="Search for skill videos..."
					value={wordEntered}
					onChange={handleFilter}
				/>
				<div className={styles.searchIcon}>
					{wordEntered === "" ? (
						<SearchIcon />
					) : (
						<CloseIcon id="clearBtn" onClick={clearInput} />
					)}
				</div>
				<button onClick={(e) => props.handleDelete(e, props.index)}
          className={styles.remove_button}
        > Remove </button>
			</div>
			{filteredData.length != 0 && (
				<div className={styles.dataResult}>
					{filteredData.slice(0, 15).map((value, key) => {
						return (
							<span className={styles.dataItem} onClick={() => handleChange(value)}>
								<p>{value.title} </p>
							</span>
						);
					})}
				</div>
			)}
		</div>
	);
}

SearchSkillAddBar.propTypes = {
	data: PropTypes.array,
	updateVideoSkill: PropTypes.func,
	index: PropTypes.number,
	preFilled: PropTypes.object,
	handleDelete: PropTypes.func
}

export default SearchSkillAddBar;
import React from 'react'
import styles from './styles/FilterContainer.module.css'
import TagLabel from './TagLabel'
import SelectedTagLabel from './SelectedTagLabel'

import Backdrop from '@mui/material/Backdrop';
import Box from '@mui/material/Box';
import Modal from '@mui/material/Modal';
import Fade from '@mui/material/Fade';

const FilterContainer = (props) => {
  
  const [tagData, setTagData] = React.useState([])

  //Modal Feature
  const [open, setOpen] = React.useState(false);
  const handleOpen = () => setOpen(true);
  const handleClose = () => setOpen(false);
  
  React.useEffect(() => {
    //Fetch all tags
    let temp = [
      {"tag_category_id" : 1, "tag_category_name": "Cuisine", "tags": [{"tag_id" : 1, "tag_name" : "Australian"},{"tag_id" : 2, "tag_name" : "Asian"},{"tag_id" : 3, "tag_name" : "Europe"}]},
      {"tag_category_id" : 2, "tag_category_name": "Meal type", "tags": [{"tag_id" : 4, "tag_name" : "Breakfast"},{"tag_id" : 5, "tag_name" : "Lunch"},{"tag_id" : 6, "tag_name" : "Dinner"}]},
      {"tag_category_id" : 3, "tag_category_name": "Difficulty", "tags": [{"tag_id" : 7, "tag_name" : "Easy"},{"tag_id" : 8, "tag_name" : "Medium"},{"tag_id" : 9, "tag_name" : "Hard"}]}
    ]
    setTagData(temp)
  }, [])

  const renderTags = () => {
    let content = [];
    for (let i = 0; i < tagData.length; i++) {
      let tagsContent = tagData[i].tags.map((object, index) => {
        const isSelected = checkIfSelected(object);
        return(<TagLabel object={object} isSelected={isSelected} clickFunction={isSelected ? removeTag : selectTag}></TagLabel>)
      })
      content.push(
        <div style={{marginTop:'10px'}}>
          <div>{tagData[i].tag_category_name}</div>
          <div className={styles.tag_container}>{tagsContent}</div>
        </div>
      )
    }
    return content
  }

  const checkIfSelected = (object) => {
		for(let i = 0; i < props.selectedTags.length; i++) {
			if (object.tag_id === props.selectedTags[i].tag_id) return true;
		}
		return false;
	}
  const selectTag = (object) => {
    props.setSelectedTags([...props.selectedTags, object])
  }
  const removeTag = (object) => {
		props.setSelectedTags(props.selectedTags.filter(selTag => {
			return selTag.tag_id !== object.tag_id;
		}))
	}
  const renderSelectedTags = (list_selected_tags) => {
    let content = list_selected_tags.map((object, index) => {
			return (<SelectedTagLabel object={object} clickFunction={removeTag} ></SelectedTagLabel>)
		})
		return content;
  }
  const renderAddTagButton = () => {
    return (<TagLabel object={{"tag_id":-1, "tag_name":"+"}} clickFunction={handleOpen}></TagLabel>)
  }

  return (
    <>
      <div >
        <Modal
          open={open}
          onClose={() => handleClose()}
          closeAfterTransition
          BackdropComponent={Backdrop}
          BackdropProps={{
            timeout: 500,
          }}
        >
          <Fade in={open}>
            <Box className={styles.modal}>
              {renderTags()}
            </Box>
          </Fade>
        </Modal>
      </div>

      <div className={styles.container}>
				<div className={styles.text}>Filter By</div>
        <div className={styles.selected_tag_container}>
          {renderAddTagButton()}
          {renderSelectedTags(props.selectedTags)}
				</div>
			</div>
    </>
  )
}

export default FilterContainer
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
    //Fetch all tag categories
    let temp = []
    for(let i = 0; i < 4; i++) {
      temp.push({"id":i, "name":"TagCategory"+i, "tags":[]})
    }
    //Fetch tags on each category
    for (let i = 0; i < temp.length; i++) {
      for (let j = 0; j < 10; j++) {
        temp[i].tags.push({"id":j, "name":"Tag"+j})
      }
    }
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
        <div style={{marginTop:'20px'}}>
          <div>{tagData[i].name}</div>
          <div className={styles.tag_container}>{tagsContent}</div>
        </div>
      )
    }
    return content
  }

  const checkIfSelected = (object) => {
		for(let i = 0; i < props.selectedTags.length; i++) {
			if (object.id === props.selectedTags[i].id) return true;
		}
		return false;
	}
  const selectTag = (object) => {
    props.setSelectedTags([...props.selectedTags, object])
  }
  const removeTag = (object) => {
		props.setSelectedTags(props.selectedTags.filter(selTag => {
			return selTag.id !== object.id;
		}))
	}
  const renderSelectedTags = (list_selected_tags) => {
    let content = list_selected_tags.map((object, index) => {
			return (<SelectedTagLabel object={object} clickFunction={removeTag} ></SelectedTagLabel>)
		})
		return content;
  }
  const renderAddTagButton = () => {
    return (<TagLabel object={{"id":-1, "name":"+"}} clickFunction={handleOpen}></TagLabel>)
  }

  return (
    <>
      <div>
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
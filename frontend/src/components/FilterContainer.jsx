import React from 'react'
import styles from './styles/FilterContainer.module.css'
import TagLabel from './TagLabel'
import SelectedTagLabel from './SelectedTagLabel'
import { APICall } from '../helperFunc'
import SquareIcon from '@mui/icons-material/Square';

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

  const getAllTags = async() => {
		let tag_cat_data = []; let tag_data =[];
		try {
			const headers = {
			  'Content-Type': 'application/json',
			};
			tag_cat_data = await APICall(null, '/search/tag/categories', 'GET', headers);
      for (let i = 0; i < tag_cat_data.tag_categories.length; i++) {
        tag_data = await APICall(null, `/search/tag/tags?tag_category_id=${tag_cat_data.tag_categories[i].category_id}`, 'GET', headers);
        tag_cat_data.tag_categories[i]['tags'] = tag_data['tags']
      }
      setTagData(tag_cat_data.tag_categories)
      
		} catch (err) {
			alert(err);
		}
  }
  
  React.useEffect(() => {
    //Fetch all tags
    getAllTags();
  }, [])

  const renderTags = () => {
    let content = [];
    for (let i = 0; i < tagData.length; i++) {
      let tagsContent = tagData[i].tags.map((object, index) => {
        const isExcluded = checkIfExcluded(object)
        const isIncluded = checkIfIncluded(object)
        return(<TagLabel object={object} isExcluded={isExcluded} isIncluded={isIncluded} clickFunction={isExcluded ? removeTag : selectTag}></TagLabel>)
      })
      content.push(
        <div style={{marginTop:'10px'}}>
          <div>{tagData[i].name}</div>
          <div className={styles.tag_container}>{tagsContent}</div>
        </div>
      )
    }
    return content
  }

  const checkIfExcluded = (object) => {
		for(let i = 0; i < props.selectedTags.length; i++) {
			if (object.tag_id === props.selectedTags[i].tag_id && props.selectedTags[i].status === 'exclude') return true;
		}
		return false;
	}

  const checkIfIncluded = (object) => {
		for(let i = 0; i < props.selectedTags.length; i++) {
			if (object.tag_id === props.selectedTags[i].tag_id && props.selectedTags[i].status === 'include') return true;
		}
		return false;
	}

  const selectTag = (object) => {
    let isIncludeFlag = false
    let i = 0
    for(; i < props.selectedTags.length; i++) {
			if (object.tag_id === props.selectedTags[i].tag_id && props.selectedTags[i].status === 'include') {
        isIncludeFlag = true
        break
      };
		}
    if (isIncludeFlag) {
      const temp = [...props.selectedTags]
      temp[i].status = 'exclude'
      props.setSelectedTags(temp)
    } else {
      let temp = {...object}
      temp.status ='include'
      props.setSelectedTags([...props.selectedTags, temp])
    }
  }

  const removeTag = (object) => {
		props.setSelectedTags(props.selectedTags.filter(selTag => {
			return selTag.tag_id !== object.tag_id;
		}))
	}

  const renderSelectedTags = (list_selected_tags) => {
    let content = list_selected_tags.map((object, index) => {
      const isExcluded = checkIfExcluded(object)
      const isIncluded = checkIfIncluded(object)
			return (<SelectedTagLabel object={object} clickFunction={removeTag} isExcluded={isExcluded} isIncluded={isIncluded} ></SelectedTagLabel>)
		})
		return content;
  }
  const renderAddTagButton = () => {
    return (<TagLabel object={{"tag_id":-1, "name":"+"}} clickFunction={handleOpen}></TagLabel>)
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
              <div style={{display: 'flex', flexDirection: 'row', justifyContent: 'space-evenly'}}>
                <div style={{display: 'flex', flexDirection: 'row', alignItems: 'center'}}>
                  <SquareIcon sx={{width: 30, height: 30, color: 'rgb(56, 235, 36)'}}/>
                  <span style={{paddingTop: '5px'}}> Include Tags </span>
                </div>
                <div style={{display: 'flex', flexDirection: 'row', alignItems: 'center'}}>
                  <SquareIcon sx={{width: 30, height: 30, color: 'red'}}/>
                  <span style={{paddingTop: '5px'}}> Exclude Tags </span>
                </div>
              </div>
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
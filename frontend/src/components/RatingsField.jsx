import React from 'react'
import styles from './styles/RatingsField.module.css'

const RatingsField = (props) => {

  const createContent = () => {
    let content = [];
    // console.log(props.statistic)
    content.push(
      <div className={styles["reviews__single_star_average"]}>
        <div className={styles["single_star_average__amount"]}> 5 star</div>
        <div className={styles["single_star_average__progress_bar"]}>
          <progress
            className={styles["progress_bar__data"]}
            max="100"
            value={5*10}
          ></progress>
        </div>
        <div className={styles["single_star_average__percentage"]}>{5*10}%</div>
      </div>
    )
    return content;
  }
  return (
    <>
      <div className={styles["reviews"]}>
        <div className={styles["reviews__breakdown"]}>
          <div className={styles["reviews_breakdown__wrapper"]}>
            {createContent()}
          </div>
        </div>
      </div>
    </>
  )
}

export default RatingsField
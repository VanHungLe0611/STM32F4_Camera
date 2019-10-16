/**
 * File              : dwt_stm32_delay.h
 * Author            : Duy Anh Pham <duyanh.y4n.pham@gmail.com>
 * Date              : 08.10.2019
 * Last Modified Date: 08.10.2019
 * Last Modified By  : Duy Anh Pham <duyanh.y4n.pham@gmail.com>
 */
#ifndef DWT_STM32_DELAY_H
#define DWT_STM32_DELAY_H

#ifdef __cplusplus
extern "C" {
#endif


//#include "stm32l4xx_hal.h"
#include "stm_hal_userconfig.h"

/**
 * @brief  Initializes DWT_Cycle_Count for DWT_Delay_us function
 * @return Error DWT counter
 *         1: DWT counter Error
 *         0: DWT counter works
 */
uint32_t DWT_Delay_Init(void);



/**
 * @brief  This function provides a delay (in microseconds)
 * @param  microseconds: delay in microseconds
 */
void DWT_Delay_us(volatile uint32_t microseconds);


#ifdef __cplusplus
}
#endif

#endif

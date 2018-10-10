/*Ensure that whenever receiveUpdate is called, 
as a consequence updateShipment of the ShipmentSearchIndex is also called once, 
with the corresponding data and id passed to it.
Also make sure that the executions of updateShipment with the same id never run concurrently
 (execution always in order and consecutive). Assume all the code is running in one NodeJS process.
*/
async function sleep(ms: number) {
  return new Promise((resolve, reject) => {
    setTimeout(() => resolve(), ms);
  });
}

async function randomDelay() {
  const randomTime = Math.round(Math.random() * 1000);
  return sleep(randomTime);
}

class ShipmentSearchIndex {
  async updateShipment(id: string, shipmentData: any) {
    const startTime = new Date();
    await randomDelay();
    const endTime = new Date();
    console.log(
      `update ${id}@${startTime.toISOString()} finished@${endTime.toISOString()}`
    );

    return { startTime, endTime };
  }
}

// Implementation needed
interface ShipmentUpdateListenerInterface {
  receiveUpdate(id: string, shipmentData: any);
}

class ShipmentUpdate implements ShipmentUpdateListenerInterface {
  async receiveUpdate(id: string, shipmentData: any) {
    let objShipmentSearchIndex = new ShipmentSearchIndex();
    await objShipmentSearchIndex.updateShipment(id, shipmentData);
  }
}

let objShipmentUpdate = new ShipmentUpdate();
objShipmentUpdate.receiveUpdate('12', null);

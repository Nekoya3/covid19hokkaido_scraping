import csv
import json
import datetime
from patients import PatientsReader

class CovidDataManager:
    def __init__(self):
        self.data = {
            'contacts':{},
            'querents':{},
            'patients':{},
            'patients_summary':{},
            'discharges':{},
            'discharges_summary':{},
            'inspections':{},
            'inspections_summary':{},
            'better_patients_summary':{},
            'last_update':datetime.datetime.now().isoformat(),
            'main_summary':{}
        }

    def fetch_data(self):
        pr = PatientsReader()
        self.data['patients'] = pr.make_patients_dict()
        self.data['patients_summary'] = pr.make_patients_summary_dict()

    def export_csv(self):
        for key in self.data:
            if key == 'last_update' or key == 'main_summary':
                continue

            datas = self.data[key]
            if datas == {}:
                continue
            
            maindatas = datas['data']
            header = list(maindatas[0].keys())
            csv_rows = [ header ]
            for d in maindatas:
                csv_rows.append( list(d.values()) )

            with open('data/' + key, 'w', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerows(csv_rows)

    def export_json(self, filepath='data/data.json'):
        with open(filepath, 'w') as f:
            json.dump(self.data, f, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    dm = CovidDataManager()
    dm.fetch_data()
    dm.export_csv()
    dm.export_json()
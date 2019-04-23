# default run, politician dataset
python src/embedding_clustering.py

# news site dataset
python src/embedding_clustering.py \
--input data/new_sites_edges.csv \
--assignment-output outputs/assignments/new_sites.json \
--embedding-output outputs/embeddings/new_sites_embedding.csv \
--cluster-mean-output outputs/cluster_means/new_sites_means.csv \
--log-output outputs/logs/new_sites.json

# HU dataset
python src/embedding_clustering.py \
--dimensions 32 --num-of-walks 20 --random-walk-length 160 --cluster-number 32 \
--input data/deezer_clean_data/HU_edges.csv \
--assignment-output outputs/assignments/HU.json \
--embedding-output outputs/embeddings/HU_embedding.csv \
--cluster-mean-output outputs/cluster_means/HU_means.csv \
--log-output outputs/logs/HU.json

# athletes dataset
python src/embedding_clustering.py \
--dimensions 32 --num-of-walks 20 --random-walk-length 160 --cluster-number 32 \
--input data/athletes_edges.csv \
--assignment-output outputs/assignments/athletes.json \
--embedding-output outputs/embeddings/athletes_embedding.csv \
--cluster-mean-output outputs/cluster_means/athletes_means.csv \
--log-output outputs/logs/athletes.json
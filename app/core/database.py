import faiss

class FaissDatabase:
    def __init__(self, index_file, d, nlist):
        self.index_file = index_file
        self.d = d
        self.nlist = nlist

        # Load the index file if it exists, otherwise create a new index
        if os.path.exists(index_file):
            self.index = faiss.read_index(index_file)
        else:
            self.index = faiss.IndexFlatL2(d)
            self.index = faiss.IndexIVFFlat(self.index, d, nlist)
            self.index.nprobe = nprobe

    def search(self, query_embedding, k):
        # Search the index for the k nearest neighbors to the query embedding
        distances, doc_ids = self.index.search(query_embedding.reshape(1, -1), k)

        return doc_ids[0]

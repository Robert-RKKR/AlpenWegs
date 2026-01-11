// Imports:
import { Pagination as MantinePagination, Center } from "@mantine/core";

// Props for Pagination component:
type Props = {
  page: number;
  pageCount: number;
  onChange: (page: number) => void;
};

// Pagination Component:
export function Pagination({ page, pageCount, onChange }: Props) {
  if (pageCount <= 1) {
    return null;
  }

  return (
    <Center>
      <MantinePagination
        value={page}
        total={pageCount}
        onChange={onChange}
        siblings={2}
        boundaries={1}
        autoContrast
        withEdges
      />
    </Center>
  );
}
